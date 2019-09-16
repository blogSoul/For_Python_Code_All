class calldata:
    def __init__(self, filepath):
        self.filepath = filepath

    def tagDClens(self):
        # 다른 사람들에게 얼마나 태그 다했는지 확인
        matrix = [[0 for col in range(5)] for row in range(10000)]

        f = open(self.filepath, "r")

        while True:
            line = f.readline()
            if not line:
                break

            line_split = line.split('\t')

            matrix[int(line_split[2]) - 1][0] = int(matrix[int(line_split[2]) - 1][0]) + 1
            #태그 얼마나 당했는지
            matrix[int(line_split[1]) - 1][1] = int(matrix[int(line_split[1]) - 1][1]) + 1
            #북마크가 얼마나 이용당했는지

        f.close()

        return matrix