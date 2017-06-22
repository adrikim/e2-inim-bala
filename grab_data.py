from bs4 import BeautifulSoup

EPSD_ENTRY_URL = 'http://psd.museum.upenn.edu/epsd/epsd/e{}.html'
ENTRY_NUMBERS = [ x for x in range(1, 6610) ]
# ENTRY_LETTERS = [ 'a', 'b', 'c', 'd', 'e', 'g', 'h', 'i', 'k', 'l', 'm', 'n',
#                  'ng', 'p', 'r', 's', 'sh', 't', 'u', 'w', 'y', 'z']


def get_entries():
    """
    Grabs all entries from each e<LETTER>s.html page and
    returns them as a list of JSONs.

    Page's format is:
    h1 .entry
        span .cf
        span .gw
    p .icount

    div .summary
        p
            a (unimportant)
            "time periods"
            span .wr (...)
                sub (for subscript #'s')
            (...)
            "description"
            span .akk (...)
        div .compounds
            p .xcpd
                "See"
                a href="javascript:showarticle('e<ID#>.html')"
                    "canon_form[guide_word]",
                (...)
    div .orth
    div .orth oview
    div .morphology
    div .senses
    div .glosses
    div .bib
    p .outlink
    """
    for x in ENTRY_NUMBERS:
        entry = { 'id': x }
        url = EPSD_ENTRY_URL.format(x)
        print("Getting entries from ", url, "...")
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser") # is the page's DOM

        # get entry's short form
        entry['canonForm'] = soup.find("h1", { "class": "entry" }).find("span", { "class": "cf" }).text.strip() # no numbers
        entry['guideWord'] = soup.find("h1", { "class": "entry" }).find("span", { "class": "gw" }).text.strip()

        # get instance count
        entry['instances'] = soup.find("p", { "class": "icount" }).text.strip().rstrip(" instances)").lstrip("(")

        # get summary
        # (399x: ED IIIb, Old Akkadian, Lagash II, Ur III, Old Babylonian, unknown)  wr. e; na-be2-a; be2; ne; da-me; na-be2; e7 "perfect plural and imperfect stem of dug[to speak]"
        summary = soup.find("div", { "class": "summary" }).find("p").text
        # NOTE all the info here is found in other sections anyway...
        # TODO get time periods (aka: ortho)
        time_peroids = []
        # TODO get ortho forms here?
        
        # get compounds
        compounds = soup.find("div", { "class": "summary" }).find("div", { "class": "compounds" }).find("p")
        entry['compounds'] = [ { a: a.text } for a in compounds.find_all("a") ] # { id#: citationForm[guideWord] }
        '''
             (<INSTANCES>x: ED IIIa, ED IIIb, Old Akkadian, Lagash II, Ur III, Early Old Babylonian, Old Babylonian)  wr.
            <span class="wr">
                a<sub>2</sub>
            </span>
             "arm; labor; wing; horn; side; strength; wage; power" Akk.&nbsp;
        '''
        # TODO get orthography
        # LOOK UP
        # TODO get orthography overview
        table = soup.find(lambda tag: tag.name == 'table' and tag.has_key('id') and tag['id'] == "oview")
        rows = talbe.findAll(lambda tag: tag.name == 'tr')

        # TODO get morphology/attested forms
        morphology = soup.find("div", { "class": "morphology" }).find("p").text

        # TODO get senses/meanings
        entry['sense'] = soup.find("div", { "class": "senses" }).find("h3", { "class": "sense" }).text.strip()
        entry['usages'] = soup.find("div", { "class": "senses" }).find("div", { "class": "usages" }).text.strip()
        # get Akkadian glosses
        akk = soup.find("div", { "class": "glosses" }).text.lstrip(".\n").rstrip("\nAkk.\xa0")
        entry['akkadian'] = []
        for k in akk.split("\"; "):
            s = k.split(" \"", 1)
            entry['akkadian'].append({ 'word': s[0], 'meaning': s[1]})
        # TODO get bibliography
        bib = soup.find("div", { "class": "bib" })
        entry['bibliography'] = [ { a: a.text } for a in compounds.find_all("p")]
        # TODO get outlinks
        outlinks = soup.find("p", { "class": "outlink" })
        if outlinks.text:


if (__name__ == "__main__"):
    get_entries()
    pass
    