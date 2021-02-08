
let tests=[
    {
        "name":"To verify Login on Orange HRM",
        "execute":"yes",
        "steps":[
            {
                "action":"launchApp",
                "args":{"url":"https://opensource-demo.orangehrmlive.com/"}
            },
            {
                "action":"login",
                "args":{
                    "username":"Admin",
                    "password":"admin123"
                }
            },
            {
                "action":"closeBrowser"
            }
        ]
    },
    {
        "name":"To verify todoApp launch",
        "execute":"no",
        "steps":[
            {
                "action":"launchApp",
                "args":{"url":"https://lambdatest.github.io/sample-todo-app/"}
            },
            {
                "action":"sleep",
                "args":{"seconds":"5"}
            },
            {
                "action":"closeBrowser"
            }
        ]
    }
];

export {tests};