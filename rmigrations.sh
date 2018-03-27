#!/usr/bin/env bash
find */migrations/* -name '000*' -print0| xargs -0 rm --