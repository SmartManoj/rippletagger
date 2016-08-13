# -*- coding: utf-8 -*-
import unittest
from rippletagger.tagger import Tagger

class TestIntegration(unittest.TestCase):
    def test_english(self):
        tagger = Tagger(language="en")
        self.assertEqual(
            tagger.tag(u"The quick brown fox jumps over the lazy dog ."),
            [
                (u'The', u'DET'),
                (u'quick', u'ADJ'),
                (u'brown', u'ADJ'),
                (u'fox', u'NOUN'),
                (u'jumps', u'VERB'),
                (u'over', u'ADP'),
                (u'the', u'DET'),
                (u'lazy', u'ADJ'),
                (u'dog', u'NOUN'),
                (u'.', u'PUNCT'),
            ]
        )

    def test_french(self):
        tagger = Tagger(language="fr")
        self.assertEqual(
            tagger.tag(u"Cette annonce a fait l' effet d' une véritable bombe ."),
            [
                (u'Cette', 'DET'),
                (u'annonce', 'NOUN'),
                (u'a', 'AUX'),
                (u'fait', 'VERB'),
                (u"l'", 'DET'),
                (u'effet', 'NOUN'),
                (u"d'", 'ADP'),
                (u'une', 'DET'),
                (u'véritable', 'ADJ'),
                (u'bombe', 'NOUN'),
                (u'.', 'PUNCT'),
            ]
        )

    def test_swedish(self):
        tagger = Tagger(language="sv")
        self.assertEqual(
            tagger.tag(u"Fördomen har alltid sin rot i vardagslivet"),
            [
                (u'Fördomen', 'NOUN'),
                (u'har', 'AUX'),
                (u'alltid', 'ADV'),
                (u'sin', 'PRON'),
                (u'rot', 'NOUN'),
                (u'i', 'ADP'),
                (u'vardagslivet', 'NOUN'),
            ]
        )

if __name__ == '__main__':
    unittest.main()
