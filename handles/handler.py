# -*- coding: utf-8 -*-
import socketserver


class Handler(socketserver.BaseRequestHandler):
    def handle(self):
        Handler.work(self)

    @staticmethod
    def set_work(work):
        Handler.work = work
