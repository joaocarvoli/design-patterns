# Example Architecture

The following diagram shows the architecture before the application of the Observer pattern:

```mermaid
---
title: Animal example
---
classDiagram
    plan <-- Main
    user <-- Main
    
    User <-- db
    db <-- user
    log <-- user
    slack <-- user
    stringtools <-- user
    email <-- user
    
    email <-- plan
    db <-- plan
    log <-- plan
    slack <-- plan
    
        namespace lib {
        class email
        class log
        class db_file
        class slack
        class stringtools
    }
    
    namespace db_file {
        class User {
        +string name
        +string email
        +string password
        +string plan
        +string reset_code
        +constructor(string name, string password, string email)
        +reset_password(string code, string new_password)
        }
        
        class db {
        +create_user(string name, string password, string email)
        +find_user(string name)
        }
    }

    class email {
        +send_email(name: str, address: str, subject: str, body: str)
    }
    
    class log {
        +log(string msg)
    }
    
    class slack {
        +post_slack_message(string channel, string msg)
    }
    
    class stringtools {
        +get_random_string(length)
    }
        
    namespace api {
        class plan {
            +upgrade_plan(string email)
        }
        
        class user {
            +register_new_user(string name, string password, string email)
            +password_forgotten(string email)
        }
    }
```