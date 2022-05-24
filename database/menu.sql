CREATE TABLE IF NOT EXISTS menu(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name VARCHAR(255) NOT NULL,
    category VARCHAR(255) NOT NULL,
    price TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS reviews(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_review VARCHAR(255) NOT NULL,
    review VARCHAR(255) NOT NULL
);

INSERT INTO menu (product_name, category, price) VALUES
    ("mizza", "pizza", "10$"),
    ("salt`lyami", "pizza", "8$"),
    ("だって好きなんだもの", "sushi", "5$"),
    ("ちょっと失礼。", "sushi", "6$"),
    ("ships little", "snacks", "1$"),
    ("ships medium", "snacks", "2$"),
    ("chips ultramegakillahardcore", "snacks", "3$");

INSERT INTO reviews (author_review, review) VALUES
    ("japanese friend", "すしがらくた https://www.youtube.com/watch?v=BleYAt1PrhA"),
    ("Anomin", "thay don`t recognized me 10\10"),
    ("Vikusya_2009(beer enjoyer)", "where`s cherry beer? 9\10");