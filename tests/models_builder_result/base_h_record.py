# generated by ModelBuilder
from scielo_migration.iid2json.meta_record import MetaRecord


# generated by ModelBuilder
class BaseArticleRecord(MetaRecord):

    def __init__(
            self, record, multi_val_tags=None,
            data_dictionary=None):
        super().__init__(
            record, multi_val_tags, data_dictionary)

    # generated by ModelBuilder
    @property
    def fulltexts(self):
        """
        Fulltexts
        v000
        """
        return self.get_field_content("v000", subfields={}, single=True, simple=True)

    # generated by ModelBuilder
    @property
    def html_url(self):
        """
        Html Url
        v000
        """
        return self.get_field_content("v000", subfields={}, single=True, simple=True)

    # generated by ModelBuilder
    @property
    def is_ahead_of_print(self):
        """
        Is Ahead Of Print
        v000
        """
        return self.get_field_content("v000", subfields={}, single=True, simple=True)

    # generated by ModelBuilder
    @property
    def issue(self):
        """
        Issue
        v000
        """
        return self.get_field_content("v000", subfields={}, single=True, simple=True)

    # generated by ModelBuilder
    @property
    def issue_label(self):
        """
        Issue Label
        v000
        """
        return self.get_field_content("v000", subfields={}, single=True, simple=True)

    # generated by ModelBuilder
    @property
    def issue_url(self):
        """
        Issue Url
        v000
        """
        return self.get_field_content("v000", subfields={}, single=True, simple=True)

    # generated by ModelBuilder
    @property
    def journal(self):
        """
        Journal
        v000
        """
        return self.get_field_content("v000", subfields={}, single=True, simple=True)

    # generated by ModelBuilder
    @property
    def mixed_affiliations(self):
        """
        Mixed Affiliations
        v000
        """
        return self.get_field_content("v000", subfields={}, single=True, simple=True)

    # generated by ModelBuilder
    @property
    def pdf_url(self):
        """
        Pdf Url
        v000
        """
        return self.get_field_content("v000", subfields={}, single=True, simple=True)

    # generated by ModelBuilder
    @property
    def translated_htmls(self):
        """
        Translated Htmls
        v000
        """
        return self.get_field_content("v000", subfields={}, single=True, simple=True)

    # generated by ModelBuilder
    @property
    def assets_code(self):
        """
        Assets Code
        v004
        """
        return self.get_field_content("v004", subfields={}, single=True, simple=True)

    # generated by ModelBuilder
    @property
    def author(self):
        """
        Author
        v010 {'1': 'xref', 'k': 'orcid', 'l': 'lattes', 'n': 'given_names', 'p': 'prefix', 'r': 'role', 's': 'surname'}
        """
        return self.get_field_content("v010", subfields={'1': 'xref', 'k': 'orcid', 'l': 'lattes', 'n': 'given_names', 'p': 'prefix', 'r': 'role', 's': 'surname'}, single=False, simple=False)

    # generated by ModelBuilder
    @property
    def corporative_authors(self):
        """
        Corporative Authors
        v011
        """
        return self.get_field_content("v011", subfields={}, single=False, simple=True)

    # generated by ModelBuilder
    @property
    def article_titles(self):
        """
        Article Titles
        v012 {'s': 'subtitle', '_': 'text', 'l': 'language'}
        """
        return self.get_field_content("v012", subfields={'s': 'subtitle', '_': 'text', 'l': 'language'}, single=False, simple=False)

    # generated by ModelBuilder
    @property
    def page(self):
        """
        Page
        v014 {'e': 'elocation', 'f': 'start', 'l': 'end', 's': 'sequence'}
        """
        return self.get_field_content("v014", subfields={'e': 'elocation', 'f': 'start', 'l': 'end', 's': 'sequence'}, single=False, simple=False)

    # generated by ModelBuilder
    @property
    def illustrative_material(self):
        """
        Illustrative Material
        v038
        """
        return self.get_field_content("v038", subfields={}, single=False, simple=True)

    # generated by ModelBuilder
    @property
    def original_language(self):
        """
        Original Language
        v040
        """
        return self.get_field_content("v040", subfields={}, single=True, simple=True)

    # generated by ModelBuilder
    @property
    def original_section(self):
        """
        Original Section
        v049
        """
        return self.get_field_content("v049", subfields={}, single=True, simple=True)

    # generated by ModelBuilder
    @property
    def section(self):
        """
        Section
        v049
        """
        return self.get_field_content("v049", subfields={}, single=True, simple=True)

    # generated by ModelBuilder
    @property
    def section_code(self):
        """
        Section Code
        v049
        """
        return self.get_field_content("v049", subfields={}, single=True, simple=True)

    # generated by ModelBuilder
    @property
    def translated_section(self):
        """
        Translated Section
        v049
        """
        return self.get_field_content("v049", subfields={}, single=True, simple=True)

    # generated by ModelBuilder
    @property
    def thesis_degree(self):
        """
        Thesis Degree
        v051
        """
        return self.get_field_content("v051", subfields={}, single=True, simple=True)

    # generated by ModelBuilder
    @property
    def thesis_organization(self):
        """
        Thesis Organization
        v052
        """
        return self.get_field_content("v052", subfields={}, single=True, simple=True)

    # generated by ModelBuilder
    @property
    def project_sponsor(self):
        """
        Project Sponsor
        v058
        """
        return self.get_field_content("v058", subfields={}, single=False, simple=True)

    # generated by ModelBuilder
    @property
    def project_name(self):
        """
        Project Name
        v059
        """
        return self.get_field_content("v059", subfields={}, single=False, simple=True)

    # generated by ModelBuilder
    @property
    def contract(self):
        """
        Contract
        v060
        """
        return self.get_field_content("v060", subfields={}, single=False, simple=True)

    # generated by ModelBuilder
    @property
    def issue_publication_date(self):
        """
        Issue Publication Date
        v065
        """
        return self.get_field_content("v065", subfields={}, single=True, simple=True)

    # generated by ModelBuilder
    @property
    def publication_date(self):
        """
        Publication Date
        v065
        """
        return self.get_field_content("v065", subfields={}, single=True, simple=True)

    # generated by ModelBuilder
    @property
    def affiliations(self):
        """
        Affiliations
        v070 {'1': 'div1', '2': 'div2', '3': 'div3', '_': 'orgname', 'c': 'city', 'e': 'email', 'i': 'id', 'p': 'country', 's': 'state'}
        """
        return self.get_field_content("v070", subfields={'1': 'div1', '2': 'div2', '3': 'div3', '_': 'orgname', 'c': 'city', 'e': 'email', 'i': 'id', 'p': 'country', 's': 'state'}, single=False, simple=False)

    # generated by ModelBuilder
    @property
    def article_type(self):
        """
        Article Type
        v071
        """
        return self.get_field_content("v071", subfields={}, single=True, simple=True)

    # generated by ModelBuilder
    @property
    def document_type(self):
        """
        Document Type
        v071
        """
        return self.get_field_content("v071", subfields={}, single=True, simple=True)

    # generated by ModelBuilder
    @property
    def abstracts(self):
        """
        Abstracts
        v083 {'a': 'text', 'l': 'language'}
        """
        return self.get_field_content("v083", subfields={'a': 'text', 'l': 'language'}, single=False, simple=False)

    # generated by ModelBuilder
    @property
    def keywords(self):
        """
        Keywords
        v085 {'k': 'text', 'l': 'language'}
        """
        return self.get_field_content("v085", subfields={'k': 'text', 'l': 'language'}, single=False, simple=False)

    # generated by ModelBuilder
    @property
    def processing_date(self):
        """
        Processing Date
        v091
        """
        return self.get_field_content("v091", subfields={}, single=True, simple=True)

    # generated by ModelBuilder
    @property
    def update_date(self):
        """
        Update Date
        v091
        """
        return self.get_field_content("v091", subfields={}, single=True, simple=True)

    # generated by ModelBuilder
    @property
    def creation_date(self):
        """
        Creation Date
        v093
        """
        return self.get_field_content("v093", subfields={}, single=True, simple=True)

    # generated by ModelBuilder
    @property
    def receive_date_iso(self):
        """
        Receive Date ISO
        v112
        """
        return self.get_field_content("v112", subfields={}, single=True, simple=True)

    # generated by ModelBuilder
    @property
    def acceptance_date_iso(self):
        """
        Acceptance Date ISO
        v114
        """
        return self.get_field_content("v114", subfields={}, single=True, simple=True)

    # generated by ModelBuilder
    @property
    def review_date_iso(self):
        """
        Review Date ISO
        v116
        """
        return self.get_field_content("v116", subfields={}, single=True, simple=True)

    # generated by ModelBuilder
    @property
    def data_model_version(self):
        """
        Data Model Version
        v120
        """
        return self.get_field_content("v120", subfields={}, single=True, simple=True)

    # generated by ModelBuilder
    @property
    def internal_sequence_id(self):
        """
        Internal Sequence Id
        v121
        """
        return self.get_field_content("v121", subfields={}, single=True, simple=True)

    # generated by ModelBuilder
    @property
    def order(self):
        """
        Order
        v121
        """
        return self.get_field_content("v121", subfields={}, single=True, simple=True)

    # generated by ModelBuilder
    @property
    def ahead_publication_date(self):
        """
        Ahead Publication Date
        v223
        """
        return self.get_field_content("v223", subfields={}, single=True, simple=True)

    # generated by ModelBuilder
    @property
    def document_publication_date(self):
        """
        Document Publication Date
        v223
        """
        return self.get_field_content("v223", subfields={}, single=True, simple=True)

    # generated by ModelBuilder
    @property
    def doi(self):
        """
        DOI
        v237
        """
        return self.get_field_content("v237", subfields={}, single=True, simple=True)

    # generated by ModelBuilder
    @property
    def normalized_affiliations(self):
        """
        Normalized Affiliations
        v240 {'i': 'id', 'p': 'country'}
        """
        return self.get_field_content("v240", subfields={'i': 'id', 'p': 'country'}, single=False, simple=False)

    # generated by ModelBuilder
    @property
    def doi_with_lang(self):
        """
        DOI with language
        v337 {'d': 'doi', 'l': 'language'}
        """
        return self.get_field_content("v337", subfields={'d': 'doi', 'l': 'language'}, single=False, simple=False)

    # generated by ModelBuilder
    @property
    def any_issn(self):
        """
        Any Issn
        v435 {'_': 'value', 't': 'type'}
        """
        return self.get_field_content("v435", subfields={'_': 'value', 't': 'type'}, single=False, simple=False)

    # generated by ModelBuilder
    @property
    def permissions(self):
        """
        Permissions
        v540
        """
        return self.get_field_content("v540", subfields={}, single=True, simple=True)

    # generated by ModelBuilder
    @property
    def languages(self):
        """
        Languages
        v601
        """
        return self.get_field_content("v601", subfields={}, single=False, simple=True)

    # generated by ModelBuilder
    @property
    def xml_languages(self):
        """
        Xml Languages
        v601
        """
        return self.get_field_content("v601", subfields={}, single=False, simple=True)

    # generated by ModelBuilder
    @property
    def scielo_domain(self):
        """
        Scielo Domain
        v690
        """
        return self.get_field_content("v690", subfields={}, single=True, simple=True)

    # generated by ModelBuilder
    @property
    def file_code(self):
        """
        File Code
        v702
        """
        return self.get_field_content("v702", subfields={}, single=True, simple=True)

    # generated by ModelBuilder
    @property
    def original_html(self):
        """
        Original Html
        v702
        """
        return self.get_field_content("v702", subfields={}, single=True, simple=True)

    # generated by ModelBuilder
    @property
    def publisher_id(self):
        """
        Publisher Id
        v880
        """
        return self.get_field_content("v880", subfields={}, single=True, simple=True)

    # generated by ModelBuilder
    @property
    def scielo_pid_v2(self):
        """
        SciELO PID v2
        v880
        """
        return self.get_field_content("v880", subfields={}, single=True, simple=True)

    # generated by ModelBuilder
    @property
    def publisher_ahead_id(self):
        """
        Publisher Ahead Id
        v881
        """
        return self.get_field_content("v881", subfields={}, single=True, simple=True)

    # generated by ModelBuilder
    @property
    def scielo_pid_v3(self):
        """
        SciELO PID v3
        v885
        """
        return self.get_field_content("v885", subfields={}, single=True, simple=True)

    # generated by ModelBuilder
    @property
    def collection_acronym(self):
        """
        Collection Acronym
        v992
        """
        return self.get_field_content("v992", subfields={}, single=True, simple=True)

