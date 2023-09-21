# Makefile for RPM Package Structure

# RPM Variables
PACKAGE_NAME := mypackage
PACKAGE_VERSION := 1.0
PACKAGE_RELEASE := 1
RPM_SPEC_FILE := $(PACKAGE_NAME).spec

# Directories
BUILD_DIR := build
SOURCES_DIR := $(BUILD_DIR)/SOURCES
BUILDROOT_DIR := $(BUILD_DIR)/BUILDROOT

.PHONY: all clean

all: rpm

# Clean build artifacts
clean:
	rm -rf $(BUILD_DIR)

# Create the RPM package structure
rpm: clean
	mkdir -p $(SOURCES_DIR) $(BUILDROOT_DIR)
	# Copy your source files to $(SOURCES_DIR)
	# For example:
	#cp  ./$(RPM_SPEC_FILE)  $(SOURCES_DIR)/
	# Create other necessary directories in BUILDROOT_DIR
	# For example:
	# mkdir -p $(BUILDROOT_DIR)/usr/bin
	# mkdir -p $(BUILDROOT_DIR)/etc
	# Create your spec file or copy it to the SOURCES directory
	# For example:
	cp mypackage.spec $(SOURCES_DIR)/
	rpmbuild -bb --define "_topdir $(BUILD_DIR)" $(SOURCES_DIR)/$(RPM_SPEC_FILE)
	mv $(BUILD_DIR)/RPMS/*/*.rpm .


