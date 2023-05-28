import requests
import os
import pandas as pd
import bs4
import keys

class KoreaDataGovAPI:
    def __init__(self, api_url, api_key):
        self.api_url = api_url
        self.api_key = api_key
    
    # 공공데이터 : 국토교통부_아파트매매_실거래자료
    # Make API call to retrieve data
    def call_api(self, params):
        response = requests.get(self.api_url, params=params)
        content = response.text
        return content


class HousingPriceData:
    def __init__(self, district, district_code):
        self.district = district
        self.district_code = district_code
        self.dataframes = []

    def create_dataframe(self, content):
        # XML 데이터 파싱 # Parse XML data
        xml_obj = bs4.BeautifulSoup(content, 'lxml-xml')
        rows = xml_obj.findAll('item')

        row_list = []  # 데이터 값들 # Data values
        name_list = []  # 컬럼 이름들 # Column names
        value_list = []  # 값들을 임시로 저장할 리스트 # Temporary list for values

        # XML 데이터에서 값을 추출하여 데이터프레임 생성
        # Extract values from XML and create a DataFrame
        for i in range(0, len(rows)):
            columns = rows[i].find_all()
            for j in range(0, len(columns)):
                if i == 0:
                    name_list.append(columns[j].name)
                value_list.append(columns[j].text)
            row_list.append(value_list)
            value_list = []

        housing_price_df = pd.DataFrame(row_list, columns=name_list)
        
        # Remove unnecessary commas in the dataframe values
        for col in housing_price_df:
            housing_price_df[col] = housing_price_df[col].astype(pd.StringDtype()).str.strip().replace(',', '', regex=True)

        # Turn transaction price column into a float dtype
        housing_price_df["거래금액"] = housing_price_df["거래금액"].astype(float)

        return housing_price_df

    def get_month_year_range(self, start_month, start_year, end_month, end_year):
        # 시작 월과 년, 종료 월과 년을 입력받아 월별로 범위 생성
        # Generate monthly range based on start month, start year, end month, and end year
        date_range = []
        ym_start = 12 * start_year + start_month - 1
        ym_end = 12 * end_year + end_month - 1
        for ym in range(ym_start, ym_end):
            y, m = divmod(ym, 12)
            y, m = str(y), str(m + 1)
            if len(m) == 1:
                m = "0" + m
            date_range.append(str(y) + str(m))
        return date_range

    def fetch_data(self, api):
        appended_df = []
        # 주어진 기간에 대한 데이터 수집
        # Fetch data for the given period of time
        for date in self.get_month_year_range(2, 2016, 4, 2023):
            params = {
                'serviceKey': api.api_key,
                'LAWD_CD': self.district_code,
                'DEAL_YMD': date
            }
            api_content = api.call_api(params)
            housing_price_df = self.create_dataframe(api_content)
            appended_df.append(housing_price_df)
        appended_housing_price_df = pd.concat(appended_df)
        self.dataframes.append(appended_housing_price_df)


class DataMerger:
    @staticmethod
    def merge_csv_files_in_directory(path, output_file):
        data_collection = []
        # 디렉토리 내의 CSV 파일들을 병합
        # Merge CSV files in the directory
        for filename in os.listdir(path):
            if filename.endswith('.csv'):
                file_path = os.path.join(path, filename)
                df = pd.read_csv(file_path)
                data_collection.append(df)
        merged_data_df = pd.concat(data_collection)
        merged_data_df.to_csv(output_file, index=False)

    @staticmethod
    def save_dataframes_to_csv(df, district, path):
        # 데이터프레임을 CSV 파일로 저장
        # Save DataFrame to CSV file
        df.to_csv(os.path.join(path, f"{district}.csv"))

def main(province_name):
    api = KoreaDataGovAPI(keys.API_URL, keys.API_KEY)
    path = f'../{province_name}Data/HousingPrices/'

    housing_data_merge = DataMerger()
    # 서울 구별 데이터 수집
    # Collect data for each district in Seoul
    for district, district_code in keys.SEOUL_DISTRCT_CODES.items():
        if not f"{district}.csv" in os.listdir(path):
            housing = HousingPriceData(district, district_code)
            housing.fetch_data(api)
            housing_data_merge.save_dataframes_to_csv(housing.dataframes[0], district, path)
