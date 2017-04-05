install:
	python setup.py install
	cp etc/wazo-admin-ui/conf.d/context.yml /etc/wazo-admin-ui/conf.d
	systemctl restart wazo-admin-ui

uninstall:
	pip uninstall wazo-admin-ui-context
	rm /etc/wazo-admin-ui/conf.d/context.yml
	systemctl restart wazo-admin-ui
