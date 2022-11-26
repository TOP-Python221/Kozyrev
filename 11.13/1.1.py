import controller

if __name__ == '__main__':
    controller.Application().start()
    email = controller.Application().ask()
    controller.Application().valid_email(email)
