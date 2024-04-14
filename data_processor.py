# data_processor.py
class DataProcessor:
    def process_data(self, raw_data):
        self.raw_data = raw_data
        processed_data = raw_data['main']['temp']
		    ## TO-DO ##
		    ## API를 통해 입력받은 json중에서 필요한 field값만 추출하기
        print(f'온도는 {processed_data}도 이다.')
        return processed_data