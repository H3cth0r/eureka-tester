# eureka-tester

Discovery Service Registration troubleshooting tool.

This tools implement easy UI for testing if eureka is working as expected.

### Example
```py
python main.py http localhost 8700 mysrevice 99000
```

```
eureka server:          http://localhost:8700/
appname:                mysrevice
instace port:           99000
              
Done
```

### User PyInstaller to compile
```
pyinstaller --onefile tool.py
```
