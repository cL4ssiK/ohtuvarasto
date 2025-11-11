import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.varasto2 = Varasto(10)
        self.varasto_yli = Varasto(10, 15)
        self.varasto_neg = Varasto(-1, -1)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)
        self.assertAlmostEqual(self.varasto_neg.tilavuus, 0)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    def test_maaritetaan_alkusaldo(self):
        self.assertAlmostEqual(self.varasto_neg.saldo, 0)
        self.assertAlmostEqual(self.varasto_yli.saldo, 10)

    def test_lisataan_neg(self):
        maara = self.varasto.saldo
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, maara)

    def test_lisataan_ylimaarin(self):
        lisataan = self.varasto.tilavuus + 5
        self.varasto.lisaa_varastoon(lisataan)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_ota_varastosta_neg(self):
        maara = self.varasto.saldo
        self.assertAlmostEqual(self.varasto.ota_varastosta(-1), 0)
        self.assertAlmostEqual(self.varasto.saldo, maara)

    def test_ota_kaikki_mita_voidaan(self):
        otetaan = self.varasto.saldo + 5
        self.assertAlmostEqual(self.varasto.ota_varastosta(otetaan), self.varasto.saldo)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_tuloste(self):
        self.assertEqual(self.varasto2.__str__(), "saldo = 0, vielä tilaa 10")

