from app import main

async def get_randomquote( quote_id: str):
    main.cursor.execute("""SELECT quote, actor FROM tbl_quotes WHERE quote_id=%s""", ( str(quote_id), ))
    return main.cursor.fetchone()

async  def get_quote( author_name: str, limit: str):
    main.cursor.execute("""SELECT  quote, actor FROM tbl_quotes WHERE actor=%s limit %s """, (author_name, limit))
    return main.cursor.fetchall()

async  def count_quotes( ):
    main.cursor.execute("""SELECT  COUNT(*) FROM tbl_quotes """)
    return main.cursor.fetchone()['count']