<<<<<<< HEAD:scielo_classic_website/models/document.py
from scielo_classic_website.isisdb.meta_record import MetaRecord
from scielo_classic_website.isisdb.h_record import ArticleRecord
=======
from scielo_migration.iid2json.meta_record import MetaRecord
from scielo_migration.isisdb.h_record import ArticleRecord
from scielo_migration.isisdb.journal_record import JournalRecord
>>>>>>> 1c656c1... Simplifica a interface de Document() que deve receber um dicionário, similar ao xylose.Article:scielo_migration/isisdb/models.py


RECORD = dict(
    o=ArticleRecord,
    h=ArticleRecord,
    f=ArticleRecord,
    l=MetaRecord,
    c=ArticleRecord,
)


<<<<<<< HEAD:scielo_classic_website/models/document.py
=======
class Journal:
    def __init__(self, journal_data):
        self._journal_record = JournalRecord(journal_data)

    def __getattr__(self, name):
        # desta forma Journal não precisa herdar de JournalRecord
        # fica menos acoplado
        if hasattr(self._journal_record, name):
            return getattr(self._journal_record, name)
        raise AttributeError(name)


>>>>>>> 1c656c1... Simplifica a interface de Document() que deve receber um dicionário, similar ao xylose.Article:scielo_migration/isisdb/models.py
class Document:
    def __init__(self, data):
        self.data = data
        self._h_record = ArticleRecord(data["article"])
        self._journal = Journal(data["title"])

    def __getattr__(self, name):
        # desta forma Document não precisa herdar de ArticleRecord
        # fica menos acoplado
        print(type(self._h_record))
        if hasattr(self._h_record, name):
            return getattr(self._h_record, name)
        raise AttributeError(name)

    @property
    def start_page(self):
        return self.page.get("start")

    @property
    def end_page(self):
        return self.page.get("end")

    @property
    def start_page_sequence(self):
        return self.page.get("sequence")

    @property
    def elocation(self):
        return self.page.get("elocation")

    @property
    def journal(self):
        return self._journal

    @property
    def translated_htmls(self):
        _translated_htmls = (self.data.get("body") or {}).copy()
        try:
            del _translated_htmls[self.original_language]
        except KeyError:
            pass
        return _translated_htmls


class DocumentRecords:
    def __init__(self, _id, records):
        self._id = _id
        self._records = None
        self.records = records

    @property
    def records(self):
        return self._records

    @records.setter
    def records(self, _records):
        self._records = {}
        for _record in _records:
            meta_record = MetaRecord(_record)
            rec_type = meta_record.rec_type
            record = RECORD[rec_type](_record)
            self._records[rec_type] = self._records.get(rec_type) or []
            self._records[rec_type].append(record)

    def get_record(self, rec_type):
        return self._records.get(rec_type)

    @property
    def article_meta(self):
        try:
            return self._records.get("f")[0]
        except TypeError:
            return None
