"""
This service handles all application requests to the database.

Its main functions are to select records and return them as a list,
or to update selected records
"""
import sqlite3
import carhire.database as db_consts
import carhire.services as services


class DBService:
    """
    DBService class to manage db executions on the carhire database
    """
    db = None
    cursor = None

    def execute_select(self, table_name, condition='', columns='*'):
        """
        Executes a select query on the specified db table and returns
        the results as a list

        :param table_name: String of the name of the db table
        :param condition: String of the condition to appear in the WHERE statement, e.g. user_id='123'
        :param columns: String of the columns, e.g. "col1" or multiple columns "col1, col2, col3"
        :return: List of returned records
        """
        services.log_service.trace("DB_SERVICE", "Executing SELECT statement: table_name(%s), condition(%s), columns(%s)" % (table_name, condition, columns))
        self.create_db_connection()
        select_query = self.generate_select_query_from_arguments(columns, table_name, condition)

        records = []
        for row in self.cursor.execute(select_query):
            records.append(row)

        self.close_db_connection()
        return records

    @staticmethod
    def generate_select_query_from_arguments(columns, table_name, condition):
        """
        Produces a complete SELECT statement to be executing using the
        arguments provided

        :param columns: String of the columns, e.g. "col1" or multiple columns "col1, col2, col3"
        :param table_name: String of the name of the db table
        :param condition: String of the condition to appear in the WHERE statement, e.g. user_id='123'
        :return: String of the complete SELECT statement
        """
        services.log_service.debug("DB_SERVICE", "Generating SELECT statement")
        select_query = "SELECT %s" % columns
        from_query = " FROM %s" % table_name
        condition_query = " WHERE %s" % condition if condition else ''
        return select_query + from_query + condition_query

    def create_db_connection(self):
        """
        Create connection to db
        """
        services.log_service.debug("DB_SERVICE", "Creating db connection")
        self.db = sqlite3.connect(db_consts.DB_NAME)
        self.cursor = self.db.cursor()

    def close_db_connection(self):
        """
        Close the cursor and db connection
        """
        services.log_service.debug("DB_SERVICE", "Closing the db connection")
        self.cursor.close()
        self.db.close()
        self.set_db_cursor_to_none()

    def commit_changes(self):
        """
        Commit the changes to the db tables
        """
        services.log_service.debug("DB_SERVICE", "Committing changes")
        self.db.commit()

    def set_db_cursor_to_none(self):
        """
        Sets the class variables to None
        """
        services.log_service.debug("DB_SERVICE", "Setting cursor and db variables to None")
        self.db = None
        self.cursor = None
