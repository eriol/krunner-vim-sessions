# Copyright 2014 Daniele Tricoli <eriol@mornie.org>

# This file is part of krunner-vim-sessions.

PLUGIN_NAME = $(shell grep X-KDE-PluginInfo-Name plugin/metadata.desktop | cut -d = -f 2)
PLUGIN_VERSION = $(shell grep X-KDE-PluginInfo-Version plugin/metadata.desktop | cut -d = -f 2)
DIST_DIR = dist
PLUGIN_ARCHIVE_ZIP = $(PLUGIN_NAME)-$(PLUGIN_VERSION).zip

.PHONY: clean install uninstall reinstall

dist:
	if [ ! -d $(DIST_DIR) ]; then mkdir $(DIST_DIR); fi
	zip -r $(DIST_DIR)/$(PLUGIN_ARCHIVE_ZIP) plugin

clean:
	rm -rf $(DIST_DIR)

install: dist
	@echo "Installing $(PLUGIN_NAME)"
	plasmapkg --type runner --install $(DIST_DIR)/$(PLUGIN_ARCHIVE_ZIP)
	kquitapp krunner
	sleep 2
	krunner

uninstall:
	plasmapkg --type runner --remove $(PLUGIN_NAME)

reinstall: uninstall clean install
