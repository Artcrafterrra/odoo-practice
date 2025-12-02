# Odoo Practice Project

A project to practice the first steps in the Odoo world.

## Overview

This repository contains a simple Odoo module (`my_practice_module`) designed to help you learn the basics of Odoo development. It demonstrates:

- **Model definition**: Creating a custom model with various field types
- **Views**: Tree, form, and search views with widgets and filters
- **Actions and menus**: Navigating your module in Odoo
- **Security**: Setting up access rights for users
- **Business logic**: Adding methods to handle state transitions

## Module Structure

```
my_practice_module/
├── __init__.py           # Module initialization
├── __manifest__.py       # Module metadata and dependencies
├── models/
│   ├── __init__.py
│   └── practice_task.py  # Practice Task model definition
├── views/
│   ├── practice_task_views.xml  # Tree, form, and search views
│   └── practice_menu.xml        # Menu items
├── security/
│   └── ir.model.access.csv      # Access rights
└── data/
    └── demo.xml                 # Demo data
```

## Installation

1. Clone this repository into your Odoo addons directory:
   ```bash
   cd /path/to/odoo/addons
   git clone https://github.com/Artcrafterrra/odoo-practice.git
   ```

2. Add the path to your Odoo configuration file or use the `--addons-path` option:
   ```bash
   ./odoo-bin --addons-path=/path/to/odoo/addons,/path/to/odoo-practice
   ```

3. Update the apps list in Odoo (Settings > Apps > Update Apps List)

4. Search for "My Practice Module" and install it

## Features

### Practice Task Model

The module includes a `practice.task` model with the following fields:

| Field | Type | Description |
|-------|------|-------------|
| name | Char | Task name (required) |
| description | Text | Task description |
| priority | Selection | Low, Normal, High, Urgent |
| state | Selection | Draft, In Progress, Done, Cancelled |
| deadline | Date | Task deadline |
| assigned_user_id | Many2one | Assigned user |
| notes | Html | Additional notes |
| active | Boolean | Archive toggle |

### Actions

The form view includes buttons to:
- **Start**: Move task from Draft to In Progress
- **Mark Done**: Complete the task
- **Cancel**: Cancel the task
- **Reset to Draft**: Reset completed/cancelled tasks

## Learning Exercises

Try these exercises to practice Odoo development:

1. **Add a new field**: Add a `tags` field using Many2many relationship
2. **Create a computed field**: Calculate days until deadline
3. **Add a constraint**: Prevent setting deadline in the past
4. **Extend the model**: Add a related model for task comments
5. **Customize the view**: Add a kanban view for the tasks

## License

LGPL-3
