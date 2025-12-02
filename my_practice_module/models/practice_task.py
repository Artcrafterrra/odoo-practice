# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PracticeTask(models.Model):
    """A simple model for practicing Odoo development."""

    _name = 'practice.task'
    _description = 'Practice Task'
    _order = 'priority desc, create_date desc'

    name = fields.Char(string='Task Name', required=True)
    description = fields.Text(string='Description')
    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Normal'),
        ('2', 'High'),
        ('3', 'Urgent'),
    ], string='Priority', default='1')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], string='State', default='draft', tracking=True)
    deadline = fields.Date(string='Deadline')
    assigned_user_id = fields.Many2one(
        'res.users',
        string='Assigned To',
        default=lambda self: self.env.user,
    )
    notes = fields.Html(string='Notes')
    active = fields.Boolean(string='Active', default=True)

    def action_start(self):
        """Mark the task as in progress."""
        self.write({'state': 'in_progress'})

    def action_done(self):
        """Mark the task as done."""
        self.write({'state': 'done'})

    def action_cancel(self):
        """Cancel the task."""
        self.write({'state': 'cancelled'})

    def action_reset_to_draft(self):
        """Reset the task to draft state."""
        self.write({'state': 'draft'})
