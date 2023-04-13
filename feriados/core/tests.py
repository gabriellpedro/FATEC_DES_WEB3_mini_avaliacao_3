from django.test import TestCase

class NatalTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/natal')
    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)
    def test_texto(self):
        self.assertContains(self.resp, 'natal')
    def test_template_natal(self):
        self.assertTemplateUsed(self.resp, 'natal.html')

class TiradentesTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/tiradentes')
    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)
    def test_texto(self):
        self.assertContains(self.resp, 'Tiradentes')
    def test_template_natal(self):
        self.assertTemplateUsed(self.resp, 'tiradentes.html')

class FeriadoModelTest(TestCase):
    def setUP(self):
        self.feriado = 'Natal'
        self.mes = 12
        self.dia = 25
        self.cadastro = FeriadoModel(            nome = self.nome,
            dia = self.dia,
            mes = self.mes,
        )
        
        self.cadastro.save()

        def test_created(self):
            self.assertTrue(FeriadoModel.object.exist())

        def test_modificado_em(self):
            self.assertIsInstance(self.cadastro.modificado_em, datetime)

        def test_nome(self):
            nome = self.cadastro.__dict__.get('nome', '')
            self.assertEqual(nome, self.feriado)

        def test_dia_feriado(self):
            dia = self.cadastro.__dict__.get('dia', '')
            self.assertEqual(dia, self.dia)