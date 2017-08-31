#!/usr/bin/env python3
import psycopg2

# Questions
que1 = '1. What are the most popular three articles of all time?'
que2 = '2. Who are the most popular article authors of all time?'
que3 = '3. On which days did more than 1% of requests lead to errors?'

# Querys
sql1 = ("select title, count(*) as views "
        "  from articles "
        " inner join log "
        "     on concat('/article/', articles.slug) = log.path "
        "  where log.status like '%200%'"
        "   group by articles.title "
        "   order by views desc limit 3;")

sql2 = ("select authors.name, count(*) as views"
        "  from articles "
        " inner join authors "
        "    on articles.author = authors.id "
        " inner join log "
        "    on concat('/article/', articles.slug) = log.path"
        " where log.status like '%200%' "
        " group by authors.name "
        " order by views desc;")

sql3 = ("select to_char(mdate,'FMMonth FMDD, YYYY'),"
        "       concat(mvalue,'%') "
        "  from ("
        "select a.day as mdate,"
        "        round(cast((100*b.hits) as numeric) / "
        "        cast(a.hits as numeric), 2) "
        "        as mvalue "
        "  from"
        "   (select date(time) as day, count(*) as hits "
        "       from log "
        "     group by day"
        "    ) as a "
        "inner join"
        "    (select date(time) as day, count(*) as hits "
        "       from log "
        "      where status "
        "        like '%404%'"
        "       group by day"
        "    ) as b "
        " on a.day = b.day) "
        " as t where mvalue > 1.0;")

# Repository Class


class Repository:
    def __init__(self):
        try:
            conn_string = """dbname=news
                             user=postgres
                             host=127.0.0.1
                             port=5432
                             password=postgres"""
            self.db = psycopg2.connect(conn_string)
            self.cursor = self.db.cursor()
        except Exception as exc:
            print(exc)

    def return_cursor(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def print_result(self, ques, query, preffix, suffix):
        query = query.replace('\n', ' ')
        result = self.return_cursor(query)
        print('')
        print(ques)
        for i in range(len(result)):
            print('\t', i + 1, '.',
                  preffix +
                  str(result[i][0]) +
                  preffix,
                  '--',
                  result[i][1],
                  suffix)

    def disconnect(self):
        self.db.close()


# Return Results
repository = Repository()
repository.print_result(que1, sql1, '"', 'views')
repository.print_result(que2, sql2, '', 'views')
repository.print_result(que3, sql3, '', 'errors')
repository.disconnect()
