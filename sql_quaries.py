import sql_connection

@sql_connection.connection_handler
def mentors_schools(cursor):
    cursor.execute("""SELECT schools.name,schools.country,first_name,last_name
                    FROM mentors
                    JOIN schools
                    ON mentors.city = schools.city
                    order by mentors.id""" )
    result = cursor.fetchall()
    return result
