#! /usr/bin/env python3

from opensubmitexec import compiler

def validate(job):
	student_files = ['lib.c','lib.h','main.c']

	result = job.run_build(inputs=student_files, output='add')
	assert(result.is_ok())

	result = job.run_compiler(inputs=student_files, output='add')
	assert(result.is_ok())

	result = job.run_make(mandatory=False)
	assert(result.is_ok())

	result = job.run_make(mandatory=True)
	assert(not result.is_ok())

	result = job.run_configure(mandatory=False)
	assert(result.is_ok())

	result = job.run_configure(mandatory=True)
	assert(not result.is_ok())
