import sql_connection

@sql_connection.connection_handler
def mentors_schools(cursor):
    cursor.execute("""SELECT schools.name as school_name,schools.country,first_name,last_name
                    FROM mentors
                    JOIN schools
                    ON mentors.city = schools.city
                    order by mentors.id""" )
    result = cursor.fetchall()
    return result


@sql_connection.connection_handler
def all_school(cursor):
    cursor.execute("""SELECT schools.name as school_name,schools.country, first_name,last_name
                    FROM mentors
                    right JOIN schools
                    ON mentors.city = schools.city
                    order by mentors.id""" )
    result = cursor.fetchall()
    return result


@sql_connection.connection_handler
def mentors_by_country(cursor):
    cursor.execute("""SELECT COUNT(schools.country), schools.country
                    FROM mentors
                    JOIN schools
                    ON mentors.city = schools.city
                    group by schools.country
                    order by schools.country""" )
    result = cursor.fetchall()
    return result


@sql_connection.connection_handler
def contacts(cursor):
    cursor.execute("""SELECT schools.name, first_name, last_name
                    FROM mentors
                    JOIN schools
                    ON mentors.id = schools.contact_person
                    order by schools.name""" )
    result = cursor.fetchall()
    return result


@sql_connection.connection_handler
def applicants(cursor):
    cursor.execute("""SELECT first_name, application_code, applicants_mentors.creation_date
                    FROM applicants
                    JOIN applicants_mentors
                    ON applicants.id = applicants_mentors.applicant_id
                    where applicants_mentors.creation_date > '2016-01-01'""" )
    result = cursor.fetchall()
    return result


@sql_connection.connection_handler
def applicants_and_mentors(cursor):
    cursor.execute("""SELECT applicants.first_name as applicants_first_name, applicants.application_code, mentors.nick_name as mentors_nick_name
                    FROM applicants
                    left JOIN applicants_mentors
                    on applicants.id = applicants_mentors.applicant_id
                    left JOIN mentors
                    on mentors.id = applicants_mentors.mentor_id""")
    result = cursor.fetchall()
    return result
