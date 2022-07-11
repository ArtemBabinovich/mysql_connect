import mysql.connector
from mysql.connector import Error


def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='your_name_db',
                                       user='your_login',
                                       password='your_password')
        if conn.is_connected():
            print('Connected to MySQL database')

        select_bid = """SELECT client_number,
                            SUM(outcome = "win") as побед,
                            SUM(outcome = "lose") as поражений
                            FROM bid
                            JOIN event_value 
                            ON bid.play_id = event_value.play_id
                            GROUP BY client_number"""

        select_event_entity = """SELECT least(home_team, away_team) AS A,
                                        greatest(home_team, away_team) AS B,
                                        COUNT(*)
                                        FROM event_entity 
                                        GROUP BY A, B
                                        ORDER BY A, B"""

        def connect_sql(sql):
            cursor = conn.cursor()
            cursor.execute(sql)
            return cursor.fetchall()

        result_select_bid = connect_sql(select_bid)
        for a in result_select_bid:
            print(a)

        result_select_event_entity = connect_sql(select_event_entity)
        for a, b, res in result_select_event_entity:
            s = f'{a} - {b}'
            print(s, f'| {res}')
    except Error as e:
        print(e)

    finally:
        conn.close()


if __name__ == '__main__':
    connect()
