import py_eureka_client.eureka_client as eureka_client
import argparse

__version__ = "0.1.0"
def show_version() -> None: print(f"version {__version__}")

def register_dummy(eurekaServer, appName, instancePort):
    try:
        eureka_client.init(eureka_server=eurekaServer, app_name=appName, instance_port=instancePort)
        print("Done")
    except Exception as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(
            description='Eureka Troubleshooting Registration tool'
    )
    group = parser.add_mutually_exclusive_group()

    group.add_argument(
        '-v', '--version',
        action='store_true',
        help='Show program version'
    )
    group.add_argument(
        '--help-examples',
        action='store_true',
        help='Show usage examples'
    )

    # main arguments
    parser.add_argument('connection', help='https or http', nargs='?')
    parser.add_argument('hostname', help='Eureka server hostname', nargs='?')
    parser.add_argument('port', help='Eureka server port', nargs='?')
    parser.add_argument('appname', help='Service name', nargs='?')
    parser.add_argument('port_service', help='Service port', nargs='?')

    args = parser.parse_args()
    
    if args.version: show_version()
    if args.help_examples:
        print("""
1. ./exe <http or https> <eureka_hostname> <eureka_port> <service_name> <service_port>
2. ./exe <http> gatewayserver 8800 my_microservice 9900
              """)
    if args.connection and args.hostname and args.port and args.appname and args.port_service:
        connection = args.connection
        eureka_server = f"{connection}://{args.hostname}:{args.port}/"
        app_name = args.appname
        instance_port = int(args.port_service)
        print(f"""
eureka server: \t\t{eureka_server}
appname:\t\t{app_name}
instace port:\t\t{instance_port}
              """)
        register_dummy(eureka_server, app_name, instance_port)

if __name__ == "__main__":
    main()
