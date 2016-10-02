# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _

class Books(models.Model):
    _name = 'library.book'
    _description = 'Book'

    name = fields.Char(string='Title')
    authors_ids = fields.Many2many(
        comodel_name="library.partner",
        string="Authors",
    )
    edition_date =  fields.Date(string='Edition date',)
    isbn = fields.Char(string='ISBN')
    publisher_id = fields.Many2one(
        'library.publisher',
        'Publisher',
    )
    rental_ids = fields.One2many(
        'library.rental',
        'book_id',
        string='Rentals',)
