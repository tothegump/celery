# task: pt
# kwargs: {'val': 't1'}
# id: 59b6e078-2f68-4c74-837c-e3ccd7d46911
# root_id: 59b6e078-2f68-4c74-837c-e3ccd7d46911
# reply_to: bca2c24e-5741-3120-b3db-4fcf2ae57521
# correlation_id: 59b6e078-2f68-4c74-837c-e3ccd7d46911
[
  [], {"val": "t1"},
  {
    "callbacks": null,
    "errbacks": null,
    "chord": null
    "chain":
    [
      {"task": "myapp.print_task",
      "args": [],
      "kwargs": {"val": "t3"},
      "options": {"task_id": "1bb40e11-80fa-4022-b348-dd61d39dcb84", "reply_to": "bca2c24e-5741-3120-b3db-4fcf2ae57521"},
      "subtask_type": null,
      "chord_size": null,
      "immutable": true
      },
      {"task": "myapp.print_task",
      "args": [],
      "kwargs": {"val": "t2"},
      "options":
        {"task_id": "98d838a7-e6ba-4335-bbef-dba89ef9c575",
        "reply_to": "bca2c24e-5741-3120-b3db-4fcf2ae57521"},
        "subtask_type": null,
        "chord_size": null,
        "immutable": true}
      ],
  }
]

# reply_to:	bca2c24e-5741-3120-b3db-4fcf2ae57521
# correlation_id:	d27ecd66-403b-42ea-84e1-5857f1a4882f
# headers:
# group:	f40c1308-2f98-431e-9cd1-e06b48750c17
# id:	d27ecd66-403b-42ea-84e1-5857f1a4882f
# kwargsrepr:	{'val': 't1'}
# root_id:	d27ecd66-403b-42ea-84e1-5857f1a4882f
# task:	myapp.print_task
[
    [], {"val": "t1"},
    {
        "callbacks": null,
        "errbacks": null,
        "chain": null,
        "chord": null
    }
]

# reply_to:	bca2c24e-5741-3120-b3db-4fcf2ae57521
# correlation_id:	299a1724-4fe5-4349-bc05-630466b89082
# headers:
# argsrepr:	()
# group:	f40c1308-2f98-431e-9cd1-e06b48750c17
# id:	299a1724-4fe5-4349-bc05-630466b89082
# kwargsrepr:	{'val': 't2'}
# root_id:	299a1724-4fe5-4349-bc05-630466b89082
# task:	myapp.print_task
[
    [], {"val": "t2"},
    {
        "callbacks": null,
        "errbacks": null,
        "chain": null,
        "chord": null
    }
]

# reply_to:	bca2c24e-5741-3120-b3db-4fcf2ae57521
# correlation_id:	2b222f1f-7b6e-4347-82d5-05cc4d0ebd08
# headers:
# argsrepr:	()
# group:	f40c1308-2f98-431e-9cd1-e06b48750c17
# id:	2b222f1f-7b6e-4347-82d5-05cc4d0ebd08
# kwargsrepr:	{'val': 't3'}
# root_id:	2b222f1f-7b6e-4347-82d5-05cc4d0ebd08
# task:	myapp.print_task
[
    [], {"val": "t3"},
    {
        "callbacks": null,
        "errbacks": null,
        "chain": null,
        "chord": null
    }
 ]


# reply_to:	bca2c24e-5741-3120-b3db-4fcf2ae57521
# correlation_id:	ce287af8-f166-4461-816e-5ff190405f8d
# headers:
# group:	b3fd0857-f2a1-42ba-9e96-147a0c47f566
# id:	ce287af8-f166-4461-816e-5ff190405f8d
# kwargsrepr:	{'val': 'c_h1'}
# root_id:	ce287af8-f166-4461-816e-5ff190405f8d
# task:	myapp.print_task
[
    [], {"val": "c_h1"},
    {
        "callbacks": null,
        "errbacks": null,
        "chain": null,
        "chord": {
            "task": "myapp.print_task",
            "args": [],
            "kwargs": {"val": "c_c3"},
            "options": {
                "task_id": "38afaf5c-8475-4b0e-8531-dfdbdedfed9a",
                "reply_to": "bca2c24e-5741-3120-b3db-4fcf2ae57521"
            },
            "subtask_type": null,
            "chord_size": 2,
            "immutable": true
        }
    }
]


# reply_to:	bca2c24e-5741-3120-b3db-4fcf2ae57521
# correlation_id:	27979076-d4ff-48bb-bf85-a617aae6b96a
# headers:
# group:	b3fd0857-f2a1-42ba-9e96-147a0c47f566
# id:	27979076-d4ff-48bb-bf85-a617aae6b96a
# kwargsrepr:	{'val': 'c_h2'}
# origin:	gen1552@tothegumpdeMacBook-Pro.local
# root_id:	27979076-d4ff-48bb-bf85-a617aae6b96a
# task:	myapp.print_task
[
    [], {"val": "c_h2"},
    {
        "callbacks": null,
        "errbacks": null,
        "chain": null,
        "chord": {
            "task": "myapp.print_task",
            "args": [],
            "kwargs": {"val": "c_c3"},
            "options": {
                "task_id": "38afaf5c-8475-4b0e-8531-dfdbdedfed9a",
                "reply_to": "bca2c24e-5741-3120-b3db-4fcf2ae57521"
            },
            "subtask_type": null,
            "chord_size": 2,
            "immutable": true
        }
    }
]




####################################################################################################
# reply_to:	bca2c24e-5741-3120-b3db-4fcf2ae57521
# correlation_id:	78791d69-a730-48df-8c95-af4692406c59
# headers:
# id:	78791d69-a730-48df-8c95-af4692406c59
# kwargsrepr:	{'val': 'pt1'}
# origin:	gen1552@tothegumpdeMacBook-Pro.local
# root_id:	78791d69-a730-48df-8c95-af4692406c59
# task:	myapp.print_task
[
    [], {"val": "pt1"},
    {
        "callbacks": null,
        "errbacks": null,
        "chain": [
            {
                "task": "celery.group",
                "args": [],
                "kwargs": {
                    "tasks": [
                        {
                            "task": "myapp.print_task",
                            "args": [],
                            "kwargs": {"val": "g1"},
                            "options": {
                                "task_id": "0fb01560-3357-429e-8967-06fccafec7da",
                                "reply_to": "bca2c24e-5741-3120-b3db-4fcf2ae57521"
                            },
                            "subtask_type": null,
                            "chord_size": null,
                            "immutable": true
                        },
                        {
                            "task": "myapp.print_task",
                            "args": [],
                            "kwargs": {"val": "g2"},
                            "options": {"task_id": "cd0ac832-2687-4470-a9d8-b95d03e49cf3", "reply_to": "bca2c24e-5741-3120-b3db-4fcf2ae57521"},
                            "subtask_type": null,
                            "chord_size": null,
                            "immutable": true
                        }
                    ]
                },
                "options": {
                    "task_id": "8b320651-10fc-4ff8-9bf9-4e8d24df3e0d",
                    "root_id": null,
                    "parent_id": null
                },
                "subtask_type": "group",
                "immutable": false,
                "chord_size": null
            }
        ],
        "chord": null
    }
]
