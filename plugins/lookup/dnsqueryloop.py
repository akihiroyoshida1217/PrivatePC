#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
import dns.resolver
from ansible.plugins.lookup import LookupBase

class LookupModule(LookupBase):
    def run(self, terms, variables=None, **kwargs):
        answers = list(set(sum([ [ a.to_text() for a in dns.resolver.query(terms[0], terms[1]) ] for i in range(20) ], [])))
        return answers

