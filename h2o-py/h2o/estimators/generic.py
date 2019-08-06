#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# This file is auto-generated by h2o-3/h2o-bindings/bin/gen_python.py
# Copyright 2016 H2O.ai;  Apache License Version 2.0 (see LICENSE for details)
#
from __future__ import absolute_import, division, print_function, unicode_literals

from h2o.estimators.estimator_base import H2OEstimator
from h2o.exceptions import H2OValueError
from h2o.frame import H2OFrame
from h2o.utils.typechecks import assert_is_type, Enum, numeric


class H2OGenericEstimator(H2OEstimator):
    """
    MOJO Model

    """

    algo = "generic"

    def __init__(self, **kwargs):
        super(H2OGenericEstimator, self).__init__()
        self._parms = {}
        names_list = {"model_id", "model_key", "path"}
        if(all(kwargs.get(name, None) is None for name in [ "model_key", "path"])):
                raise H2OValueError("At least one of [\"model_key\", \"path\"] is required.")
        if "Lambda" in kwargs: kwargs["lambda_"] = kwargs.pop("Lambda")
        for pname, pvalue in kwargs.items():
            if pname == 'model_id':
                self._id = pvalue
                self._parms["model_id"] = pvalue
            elif pname in names_list:
                # Using setattr(...) will invoke type-checking of the arguments
                setattr(self, pname, pvalue)
            else:
                raise H2OValueError("Unknown parameter %s = %r" % (pname, pvalue))

    @property
    def model_key(self):
        """
        Key to the self-contained model archive already uploaded to H2O.

        Type: ``H2OFrame``.
        """
        return self._parms.get("model_key")

    @model_key.setter
    def model_key(self, model_key):
        self._parms["model_key"] = H2OFrame._validate(model_key, 'model_key')


    @property
    def path(self):
        """
        Path to file with self-contained model archive.

        Type: ``str``.
        """
        return self._parms.get("path")

    @path.setter
    def path(self, path):
        assert_is_type(path, None, str)
        self._parms["path"] = path


    def _requires_training_frame(self):
        """
        Determines if Generic model requires a training frame.
        :return: False.
        """
        return False

    @staticmethod
    def from_file(file=str):
        """
        Creates new Generic model by loading existing embedded model into library, e.g. from H2O MOJO.
        The imported model must be supported by H2O.
        :param file: A string containing path to the file to create the model from
        :return: H2OGenericEstimator instance representing the generic model
        """
        model = H2OGenericEstimator(path = file)
        model.train()

        return model
