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
    _db = None
    _cursor = None

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
        for row in self._cursor.execute(select_query):
            records.append(row)

        services.log_service.trace("DB_SERVICE", "Returned %s rows" % (len(records)))

        self.close_db_connection()
        return records

    def execute_update(self, table_name, values, condition):
        """
        Executes a select query on the specified db table and returns
        the results as a list

        :param table_name: String of the name of the db table
        :param values: String of the values, e.g. "foo='bar'" or multiple columns "foo1='bar1', foo2='bar2', foo3='bar3'"
        :param condition: String of the condition to appear in the WHERE statement, e.g. user_id='123'
        """
        services.log_service.trace("DB_SERVICE",
                                   "Executing UPDATE statement: table_name(%s), values(%s), condition(%s)" % (
                                    table_name, values, condition))
        self.create_db_connection()

        update_query = self.generate_update_query_from_arguments(table_name, values, condition)
        services.log_service.debug("DB_SERVICE", "UPDATE query: %s" % update_query)
        self._cursor.execute(update_query)

        self.commit_changes()
        self.close_db_connection()

    @staticmethod
    def generate_update_query_from_arguments(table_name, values, condition):
        """
        Produces an UPDATE query string to be executed using the arguments provided

        :param table_name: String of the name of the db table
        :param values: String of the values, e.g. "foo='bar'" or multiple columns "foo1='bar1', foo2='bar2', foo3='bar3'"
        :param condition: String of the condition to appear in the WHERE statement, e.g. user_id='123'
        :return: String of the complete UPDATE statement
        """
        services.log_service.debug("DB_SERVICE", "Generating UPDATE statement")
        update_query = "UPDATE %s" % table_name
        set_query = " SET %s" % values
        where_query = " WHERE %s" % condition
        return update_query + set_query + where_query

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
        full_query = select_query + from_query + condition_query
        services.log_service.debug("DB_SERVICE", "Returning: %s" % full_query)
        return full_query

    def create_db_connection(self):
        """
        Create connection to db
        """
        services.log_service.debug("DB_SERVICE", "Creating db connection")
        self._db = sqlite3.connect(db_consts.DB_NAME)
        self._cursor = self._db.cursor()

    def close_db_connection(self):
        """
        Close the cursor and db connection
        """
        services.log_service.debug("DB_SERVICE", "Closing the db connection")
        self._cursor.close()
        self._db.close()
        self.set_db_cursor_to_none()

    def commit_changes(self):
        """
        Commit the changes to the db tables
        """
        services.log_service.debug("DB_SERVICE", "Committing changes")
        self._db.commit()

    def set_db_cursor_to_none(self):
        """
        Sets the class variables to None
        """
        services.log_service.debug("DB_SERVICE", "Setting cursor and db variables to None")
        self._db = None
        self._cursor = None
