from abc import ABCMeta, abstractmethod
import json

env = 'test'

class CustomerList(metaclass=ABCMeta):
    
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def fetch(self):
        pass


class CustomerTable(CustomerList):

    def __init__(self):
        self.data = self.fetch()

    def get_all(self):
        print(self.data)
        return self.data
    
    def fetch(self):
        # 本来はAPI通信で取得してくる想定
        return [
            {'name': '田中一郎', 'gender': 'male'},
            {'name': '鈴木二郎', 'gender': 'male'},
            {'name': '山田花子', 'gender': 'female'},
            {'name': '太田武', 'gender': 'male'},
            {'name': '山岡涼子', 'gender': 'female'}
        ]


class TestCustomerTable(CustomerList):

    def __init__(self):
        self.data = self.fetch()

    def get_all(self):
        print('get_allのテスト実行')
        print(self.data)
        return self.data
    
    def fetch(self):
        # 本来はテスト用のファイルロード等から取得してくる想定
        return [
            {'name': 'テスト一郎', 'gender': 'male'},
            {'name': 'テスト二郎', 'gender': 'male'},
            {'name': 'テスト花子', 'gender': 'female'}
        ]


class Serializer(metaclass=ABCMeta):
    
    @abstractmethod
    def serialize(self, data):
        pass


class JsonSerializer(Serializer):

    def serialize(self, data):
        return json.dumps(data)


class TestJsonSerializer(Serializer):

    def serialize(self, data):
        print('serializeのテスト実行')
        return json.dumps(data)


class CustomerListAbstractFactory(metaclass=ABCMeta):
    
    @abstractmethod
    def create_customer_table(self):
        pass

    @abstractmethod
    def create_serializer(self):
        pass


class CustomerTableFactory(CustomerListAbstractFactory):

    def create_customer_table(self):
        return CustomerTable()

    def create_serializer(self):
        return JsonSerializer()


class TestCustomerTableFactory(CustomerListAbstractFactory):

    def create_customer_table(self):
        return TestCustomerTable()

    def create_serializer(self):
        return TestJsonSerializer()


if env != "test":
    factory = CustomerTableFactory()
else:
    factory = TestCustomerTableFactory()

CUSTOMER_TABLE = factory.create_customer_table()
RESULT = CUSTOMER_TABLE.get_all()
SERIARIZER = factory.create_serializer()
print(SERIARIZER.serialize(RESULT))