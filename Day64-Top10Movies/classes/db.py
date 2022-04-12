from sqlalchemy import Table, Column, String, select, update, insert, create_engine, MetaData, \
    Integer, Text, Float, delete, func

# *** This is Db class for Database interaction  *** #

DB_PATH = "sqlite:///D:\\__Projects\\mojiProjekti\python\\100DaysOfCode\\Day64-Top10Movies\\movie_list.db"


class Db:
    movie_table = ""

    def __init__(self):
        self.engine = create_engine(DB_PATH)
        self.metadata = MetaData()

    def create_movie_table(self):
        self.movie_table = Table(
            "Movie",
            self.metadata,
            Column("id", Integer, primary_key=True, unique=True),
            Column("title", String(length=250), unique=True),
            Column("year", Integer),
            Column("description", Text),
            Column("rating", Float(precision=1, decimal_return_scale=2)),
            Column("ranking", Integer),
            Column("review", String(length=250)),
            Column("img_url", String(length=250))
        )

    def number_of_movies(self):
        stmt = select(func.count()).select_from(self.movie_table)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            for num in result:
                return num.count_1

    def set_ranking_numbers(self):
        stmt = select(self.movie_table).order_by(self.movie_table.c.rating.asc())
        ranking_number = self.number_of_movies()
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            for row in result:
                update_stmt = update(self.movie_table).where(self.movie_table.c.id == row.id).values(
                    ranking=ranking_number)
                conn.execute(update_stmt)
                ranking_number -= 1

    def get_movie_row(self):
        self.set_ranking_numbers()
        all_movies = []
        select_movies = select(self.movie_table).order_by(self.movie_table.c.ranking.desc())
        with self.engine.connect() as conn:
            result = conn.execute(select_movies)
            for movie in result:
                all_movies.append(movie)
        return all_movies

    def update_movie(self, review, title):
        stmt = update(self.movie_table).where(self.movie_table.c.title == title).values(review=review)
        with self.engine.connect() as conn:
            conn.execute(stmt)

    def delete_movie(self, movie_id):
        stmt = delete(self.movie_table).where(self.movie_table.c.id == movie_id)
        with self.engine.connect() as conn:
            conn.execute(stmt)

    def insert_movie(self, title, rating, year, img_url, description):
        stmt = insert(self.movie_table).values(title=title,
                                               rating=rating,
                                               year=year,
                                               img_url=f"https://image.tmdb.org/t/p/original{img_url}",
                                               description=description)
        with self.engine.connect() as conn:
            conn.execute(stmt)
