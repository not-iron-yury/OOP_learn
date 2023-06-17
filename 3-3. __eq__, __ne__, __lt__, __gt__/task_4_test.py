from unittest import TestCase, main

from task_4 import Version


class Version_test(TestCase):
    def test_eq(self):
        self.assertEquals(Version('3'), Version('3.0'))
        self.assertEquals(Version('3'), Version('3.0.0'))
        self.assertEquals(Version('3.0'), Version('3.0.0'))

    def test_ne(self):
        self.assertNotEquals(Version('3.1'), Version('3.0'))
        self.assertNotEquals(Version('3.5'), Version('3.0.0'))

    def test_lt_le(self):
        self.assertFalse(Version('3.0.3') < Version('1.11.28'))
        self.assertFalse(Version('3.0.3') <= Version('1.11.28'))

    def test_gt_ge(self):
        self.assertTrue(Version('3.0.3') > Version('1.11.28'))
        self.assertTrue(Version('3.0.3') >= Version('1.11.28'))

    def test_min_max(self):
        versions = [Version('162.5'), Version('68.3'), Version('173.8'), Version('108.9'), Version('159.6'),
                    Version('145.7'),
                    Version('187.6'), Version('137.7'), Version('33.7'), Version('22.4'), Version('199.4'),
                    Version('122.1'),
                    Version('47.4'), Version('10.2'), Version('164.9'), Version('191.6'), Version('139.9'),
                    Version('184.4'),
                    Version('94.9'), Version('188.6'), Version('56.8'), Version('138.7'), Version('83.2'),
                    Version('59.4'),
                    Version('189.7'), Version('128.5'), Version('6.6'), Version('111.2'), Version('5.6'),
                    Version('188.8'),
                    Version('64.9'), Version('76.6'), Version('85.5'), Version('195.6'), Version('12.8'),
                    Version('66.7'),
                    Version('121.7'), Version('20.3'), Version('9.8'), Version('140.8'), Version('70.3'),
                    Version('12.3'),
                    Version('97.9'), Version('10.4'), Version('98.5'), Version('74.1'), Version('164.8'),
                    Version('55.1'),
                    Version('147.7'), Version('39.2'), Version('27.4'), Version('50.3'), Version('174.7'),
                    Version('196.9'),
                    Version('106.3'), Version('89.1'), Version('59.9'), Version('189.4'), Version('45.7'),
                    Version('158.2'),
                    Version('147.5'), Version('3.2'), Version('49.9'), Version('173.6'), Version('63.9'),
                    Version('8.2'),
                    Version('29.4'), Version('15.7'), Version('85.2'), Version('109.2'), Version('152.9'),
                    Version('49.6'),
                    Version('53.5'), Version('26.7'), Version('135.9'), Version('155.3'), Version('134.7'),
                    Version('159.4'),
                    Version('99.3'), Version('188.9'), Version('197.4'), Version('99.2'), Version('160.5'),
                    Version('183.7'),
                    Version('74.2'), Version('184.7'), Version('139.8'), Version('199.2'), Version('122.1'),
                    Version('198.7'),
                    Version('190.1'), Version('200.2'), Version('40.3'), Version('150.4'), Version('20.2'),
                    Version('186.7'),
                    Version('47.2'), Version('57.5'), Version('72.8'), Version('23.1')]
        self.assertEquals(min(versions),  Version('3.2.0'))
        self.assertEquals(max(versions),  Version('200.2.0'))

    def test_print(self):
        self.assertEquals(Version('3').__str__(), '3.0.0')
        self.assertEquals(Version('3.0').__str__(), '3.0.0')
        self.assertEquals(Version('3').__repr__(), f"Version('3.0.0')")
        self.assertEquals(Version('3.0').__repr__(), f"Version('3.0.0')")

    def test_notimplemented(self):
        self.assertEquals(Version('3') == '2', False)
