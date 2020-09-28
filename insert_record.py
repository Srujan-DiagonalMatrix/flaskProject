from catalog_db import db, Publication

#pub = Publication(100, 'Oxford Publications')
paramount = Publication(102,'Paramount Press')
oracle = Publication(103,'Oracle Inc')

#db.session.add(pub)
db.session.add_all([paramount, oracle])
db.session.commit()
