# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2013 CERN.
##
## Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""Template context function to get fulltext snippets via Solr."""

from invenio.config import CFG_WEBSEARCH_FULLTEXT_SNIPPETS
from invenio.errorlib import register_exception
from invenio.bibformat_utils import get_pdf_snippets
from invenio.search_engine_utils import get_fulltext_terms_from_search_pattern


def template_context_function(id_bibrec, pattern, current_user):
    """
    @param id_bibrec ID of record
    @param pattern search pattern
    @param current_user user object
    @return HTML containing snippet
    """
    if id_bibrec and pattern and current_user:
        # Requires search in fulltext field
        if CFG_WEBSEARCH_FULLTEXT_SNIPPETS and 'fulltext:' in pattern:
            terms = get_fulltext_terms_from_search_pattern(pattern)
            if terms:
                snippets = ''
                try:
                    snippets = get_pdf_snippets(id_bibrec, terms, current_user).decode('utf8')
                except:
                    register_exception()
                return snippets
        else:
            return ''
    else:
        return None
