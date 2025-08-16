services:
  - type: web
    name: bug-bot
    env: node
    repo: https://github.com/alex96656/Alex-bugbot
    branch: main
    buildCommand: npm install
    startCommand: node index.js
    autoDeploy: true