import os.path


class ResponseFileRepository:
    @staticmethod
    def get_by_activity_type(activity_type: int) -> str:
        return ResponseFileRepository.__get_data_file(activity_type)

    @staticmethod
    def set_by_activity_type(activity_type: int, value: str) -> None:
        ResponseFileRepository.__set_data_file(activity_type, value)

    @staticmethod
    def __get_data_file(activity_type):
        f_name = os.path.join(os.path.dirname(__file__), 'id_{}.data'.format(activity_type))
        if os.path.isfile(f_name):
            f = open(f_name, 'r')
        else:
            f = open(f_name, 'w+')

        data = f.read()
        f.close()
        return data

    @staticmethod
    def __set_data_file(activity_type, data):
        f = open(os.path.join(os.path.dirname(__file__), 'id_{}.data'.format(activity_type)), 'w')
        f.write(data)
        f.close()
