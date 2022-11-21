import model
import view


class Application:
    def __init__(self):
        self.stdin_email = None

    @staticmethod
    def start():
        view.start_view()

    def ask(self):
        view.exit_answer()
        self.stdin_email = view.answer_view()
        return self.stdin_email

    @staticmethod
    def valid_email(email):
        email = email
        if email != '':
            try:
                instance_class_email = model.Email(email)
                if instance_class_email:
                    instance_class_email.save()
                    view.show_result()
                    new_email = Application().ask()
                    Application.valid_email(new_email)
            except ValueError:
                view.no_valid_email()
                new_email = Application().ask()
                Application().valid_email(new_email)
        else:
            Application().end_view()

    @staticmethod
    def end_view():
        view.end_view()

    @staticmethod
    def no_valid_email():
        view.end_view()

    @staticmethod
    def show_result():
        view.show_result()
