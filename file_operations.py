# coding=utf-8


class FileOperation(object):

    @staticmethod
    def compare_two_files(file_path1, file_path2, output_path, operation, outputSwitch):
        global result, n
        line_set1 = set(open(file_path1, 'r', encoding='UTF-8').readlines())
        line_set2 = set(open(file_path2, 'r', encoding='UTF-8').readlines())

        if '-' == operation:
            result = line_set1 - line_set2
            n = len(result)
            print('文件差集有' + str(n) + '行')
        elif '&' == operation:
            result = line_set1 & line_set2
            n = len(result)
            print("文件交集有" + str(n) + '行')
        if 1 < n < 100:
            for item in result:
                print(item)
        if outputSwitch:
            f = open(output_path, 'w', encoding='UTF-8')
            f.writelines(result)
            f.close()
            print('结果集已保存到' + output_path)
        return result


if __name__ == '__main__':
    fail_path1 = 'D:\waci\interest_0424'
    fail_path2 = 'D:\waci\select_dimension_key_dimension_value_fro.csv'
    path = 'D:\waci\esult.txt'
    FileOperation.compare_two_files(fail_path1, fail_path2, path, '-', True)
