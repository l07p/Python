# This file is definitions of all classes and their methods of Database
class cls_DB:
    """Class database is name as cls_DB"""
    def __init__(self, fileName, fileForm):
        """
        :param fileName: database file name with total path
        :param fileForm: mdb, sql, accdb, etc. it is also file extension
        """
        self.name = ""
        self.fileName = fileName
        self.file = fileForm


if __name__ == "__main__":
    anyDB = cls_DB('C:\tmp\sample','mdb')
    print(hello.)
