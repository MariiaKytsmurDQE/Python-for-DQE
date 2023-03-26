from datetime import datetime
import sqlite3
import pathlib
import os
import xmltodict
import json
import Hometask_4_3 as Normalization_module

PATH = os.path.join(pathlib.Path.cwd(), 'newsfeed.txt')
print(PATH)


# Create parent class with parameters and methods which will be used in every child class
# The 'body' parameter will be overwritten several times and in the final form
# will be equal to the value of the entire publication that will be written to the file
class Publication:
    def __init__(self, data_type, text_data='', body='', path='', filename=''):
        self.data_type = data_type
        self.text_data = text_data
        self.body = body
        self.path = path
        self.filename = filename

    # Function that add body of publication to db
    @staticmethod
    def write_to_db(data_list):
        def create_table(conn, create_table_sql_list):
            try:
                c = conn.cursor()
                for table in create_table_sql_list:
                    c.execute(table)
                return True
            except Exception as e:
                print(f'def create_table :  {e}')

        def insert_data(conn):
            try:
                c = conn.cursor()
                data_list[0] = data_list[0].lower()
                if data_list[0] == 'news':
                    c.execute("INSERT INTO news VALUES(?);", (data_list[1], ))
                elif data_list[0] == 'private ad':
                    c.execute("INSERT INTO private_Ad VALUES(?);", (data_list[1], ))
                elif data_list[0] == 'useful tips':
                    c.execute("INSERT INTO useful_tips VALUES(?);", (data_list[1], ))

            except Exception as e:
                print(f'def insert_data :  {e}')

        database = r'./sqltestdb.db'

        sql_create_news_table = """ CREATE TABLE IF NOT EXISTS news (
                                            body text_data
                                        ); """

        sql_create_private_ad_table = """CREATE TABLE IF NOT EXISTS private_ad (
                                        body text_data
                                    );"""

        sql_create_useful_tips_table = """CREATE TABLE IF NOT EXISTS useful_tips (
                                            body text_data
                                      );"""

        # Create a database connection
        conn = None
        try:
            conn = sqlite3.connect(database)
        except Exception as e:
            print(e)

        if conn is not None:
            # Create tables if not exist
            create_table(conn, [sql_create_news_table, sql_create_private_ad_table, sql_create_useful_tips_table])
            print('Tables created.')
            insert_data(conn)
            conn.commit()
            conn.close()

        else:
            raise Exception("Error! cannot create the database connection.")

    # Function that add body of publication to file
    def write_to_file(self):
        print(f'\nINFO. NewPublicationObject:\n{self.body}')
        try:
            with open(self.path + 'newsfeed.txt', 'a') as f:
                f.write(self.body + '\n\n\n')
                f.close()
            print('INFO. Successful. New publication added.')
            return True
        except Exception as e:
            print(f'ERROR. Fail. New publication was not added. Error: {e}')
            return False

    # Function that will create a new 'body'(entire publication) for every data_type of publication
    def publishing(self, save_to_db=False):
        def p1():
            object = News(data_type=self.data_type, text_data=self.text_data, body=self.body, city=input('City: '))

            if save_to_db is True:
                Publication.write_to_db([self.data_type, object.body])
                print('Data stored in db')

            return object.body

        def p2():
            object = PrivateAd(data_type=self.data_type, text_data=self.text_data, body=self.body)

            if save_to_db is True:
                Publication.write_to_db([self.data_type, object.body])
                print('Looks like data stored in db')

            return object.body

        def p3():
            object = UsefulTips(data_type=self.data_type, text_data=self.text_data, body=self.body,
                                author=input('Author: '))

            if save_to_db is True:
                Publication.write_to_db([self.data_type, object.body])
                print('Looks like data stored in db')

            return object.body
        try:
            # Create a dict where keys are data_types of publications, values are functions created above
            self.body = {"NEWS": p1, "PRIVATE AD": p2, "USEFUL TIPS": p3}[
                self.data_type]()  # The function is called right here
        except Exception as e:
            print(f'\nERROR. Incorrect publishing data_type. Available data_types (News, Private Ad, Useful Tips). '
                  f'Error: {e}')
            return False

        # Call other method-function of the class from here
        return True if Publication.write_to_file(self) else False


# Child class News with new parameters
class News(Publication):
    def __init__(self, text_data, data_type, city, body, date_time=datetime.now().strftime("%d/%m/%Y, %H:%M")):
        # The super() function is used to give access to methods and properties of a parent class.
        super().__init__(data_type, text_data, body)
        self.city = city
        self.date_time = date_time
        self.body = f'News -------------------------\n{self.text_data}\n{self.city.casefold().capitalize().strip()}, ' \
                    f'{self.date_time}\n------------------------------'


# Child class PrivateAd with new parameters
class PrivateAd(Publication):
    def __init__(self, data_type, text_data, body):
        super().__init__(data_type, text_data, body)
        self.date_delta = PrivateAd.delta_time()
        self.body = f'Private Ad -------------------\n{self.text_data}\nActual until: ' \
                    f'{self.date_delta} days\n------------------------------'

    @staticmethod
    def delta_time():
        str_d1 = input('Please input "Actual until" date in format d/m/Y: ')

        try:
            # Convert string data data_type to datetime data_type for inputted date
            d1 = datetime.strptime(str_d1, "%d/%m/%Y")
        except Exception as e:
            print(f'ERROR. Enter date in followed format next time: d/m/Y. Error: {e}')
            return False

        # Double conversion for publishing date (datetime-string-datetime)
        d2 = datetime.now().strftime("%d/%m/%Y")
        dt_object = datetime.strptime(d2, "%d/%m/%Y")

        # Difference between dates in timedelta
        delta = d1 - dt_object

        return str(delta.days)


# Child class UsefulTips with new parameters
class UsefulTips(Publication):
    def __init__(self, data_type, text_data, body, author):
        super().__init__(data_type, text_data, body)
        self.author = author
        self.body = f'Useful Tips ------------------\n{self.text_data}\nAuthor: ' \
                    f'{self.author.casefold().capitalize().strip()}\n------------------------------'


# New class that take rows(text_data) from file
class PublFromFile:
    def __init__(self, cnt_sent, filename, path=os.path.join(pathlib.Path.cwd())):
        self.cnt_sent = int([len((open(path + filename, 'r')).readlines()) if cnt_sent in [''] else cnt_sent][0])
        self.filename = filename
        self.path = path

    def read_file(self):
        # Read file
        if self.filename in os.listdir():
            def check_path():
                with open(os.path.join(self.path, self.filename), 'r') as f:
                    rows_from_file = [str(i) for i in f.readlines()]
                    print('Lines successfully read')
                return rows_from_file

            try:
                rows_from_file = check_path()
            except Exception as e:
                print(f'{e}\nCurrent path is {self.path + self.filename}')
                input('Please, enter correct path: ')
                rows_from_file = check_path()

            # Remove file
            if input('Delete file? Yes|No \n').upper() == 'Yes':
                try:
                    os.remove(self.path + self.filename)
                    print('File successfully deleted ')
                except Exception as e:
                    print('File not deleted ')
                    print(e)
            else:
                pass

            # Create text_data from file lines according to the number specified by the user
            if self.cnt_sent == 1:
                text_data_body = ''.join(rows_from_file[:1])
            else:
                text_data_body = ''.join(rows_from_file[:int(self.cnt_sent)])

            n = text_data_body
            result = Normalization_module.normalization(n)
            print(result)
            return result

        else:
            raise Exception(f'File {self.filename} not founded')


class PublFromJsonFile:
    def __init__(self, count_sentences=0, filename='', path=os.path.join(pathlib.Path.cwd())):
        self.count_elements = count_sentences
        self.filename = filename
        self.path = path

    # Read file
    def read_json(self):
        if self.filename in os.listdir():
            def check(self, f):
                if self.count_elements == '':
                    self.count_elements = len(f)

                if int(self.count_elements) > int(len(f)):
                    raise Exception('len file < count elements')
                else:
                    return self.count_elements

            def body_data_types(f):
                output_list = []
                for i in range(0, int(self.count_elements)):
                    element = f[i]
                    if element["data_type"].lower() == 'news':
                        body = f"News -------------------------\n{element['text_data']}\n{element['City']}, " \
                               f"{element['Date']}\n------------------------------"
                        output_list.append(body)
                    elif element["data_type"].lower() == 'private_ad':
                        body = f"Private Ad -------------------\n{element['text_data']}\nActual until: " \
                               f"{element['Date']} days\n------------------------------"
                        output_list.append(body)
                    elif element["data_type"].lower() == 'useful_tips':
                        body = f'Useful Tips ------------------\n{element["text_data"]}\nAuthor: ' \
                               f'{element["Author"]}\n------------------------------'
                        output_list.append(body)
                    else:
                        raise Exception(f'data_type not founded')
                return output_list

            f = json.load(open(f'{self.path}/{self.filename}'))
            check(self, f)

            if input('Delete file? Yes|No \n').upper() == 'Yes':
                try:
                    os.remove(self.path + self.filename)
                    print('File successfully deleted ')
                except Exception as e:
                    print('File not deleted ')
                    print(e)

            return '\n\n'.join(body_data_types(f))

        else:
            raise Exception(f'File {self.filename} not founded')


class PublFromXMLFile:
    def __init__(self, count_sentences=0, filename='', path=os.path.join(pathlib.Path.cwd())):
        self.count_elements = count_sentences
        self.filename = filename
        self.path = path

    def read_xml(self):
        def dict_from_xml():
            with open(self.path + self.filename) as xml_file:
                data_dict = xmltodict.parse(xml_file.read())

            return data_dict

        def body_data_types(data_dict):
            output_list = []
            i = 0
            try:
                for element in data_dict['publication_from_xml']['publication']:
                    i += 1
                    if i > self.count_elements:
                        break

                    if element["data_type"].lower() == 'news':
                        body = f"News -------------------------\n{element['text_data']}\n" \
                               f"{element['city_date']}\n------------------------------"
                        output_list.append(body)
                    elif element["data_type"].lower() == 'private_ad':
                        body = f"Private Ad -------------------\n{element['text_data']}\n" \
                               f"{element['date']}\n------------------------------"
                        output_list.append(body)
                    elif element["data_type"].lower() == 'useful_tips':
                        body = f'Useful Tips ------------------\n{element["text_data"]}\n' \
                               f'{element["author"]}\n------------------------------'
                        output_list.append(body)
                    else:
                        raise Exception(f'data_type not founded')

                # Remove file
                os.remove(self.path + self.filename)
                print('File successfully deleted ')
            except Exception as e:
                print(f'Error: {e}')
                return output_list
            return output_list

        return '\n\n\n'.join(body_data_types(dict_from_xml()))


if __name__ == '__main__':
    if input('text_data from file? Yes/No ').capitalize() == 'No':
        if input('Save results to db after processing? Yes/No ').capitalize() == 'Yes':
            store_db_param = True
        else:
            store_db_param = False

        new_publication_object = Publication(input('Choose what you want to publish '
                                                   '(News, Private Ad, Useful Tips): ').upper().strip(),
                                             input('text_data: '))
        new_publication_object.publishing(store_db_param)

    else:
        data_type_of_file = input('JSON/XML/TXT? ').upper()

        if data_type_of_file == 'JSON':
            new_object = PublFromJsonFile(int(input('Cnt publications? ')), input('Filename? '))
            text_data = new_object.read_json()
            new_publication_object = Publication('', body=text_data)
            new_publication_object.write_to_file()

        elif data_type_of_file == 'XML':
            new_object = PublFromXMLFile(int(input('Cnt publications? ')), input('Filename? '))
            text_data = new_object.read_xml()
            new_publication_object = Publication('', body=text_data)
            new_publication_object.write_to_file()

        else:
            new_object = PublFromFile(input('Cnt sentences? '), input('Filename? '))
            text_data = new_object.read_file()
            new_publication_object = Publication(input('Choose what you want to publish '
                                                       '(News, Private Ad, Useful Tips): ').upper().strip(), text_data)
            new_publication_object.publishing()
