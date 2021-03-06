import connexion
import json
import six

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.body1 import Body1  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server import util
from swagger_server.business_logic.save_data import SaveData
from swagger_server.business_logic.delete_data import DeleteData
from swagger_server.business_logic.update_data import UpdateData
from swagger_server.business_logic.get_prediction import GetPrediction
from swagger_server.business_logic.get_current_data import GetCurrentData


def retrieve_data_get(xstart=None, ystart=None, limit=None):  # noqa: E501
    """Returns the current uploaded dataset

    it will return the current dataset in json format # noqa: E501

    :param xstart:
    :type xstart: int
    :param ystart:
    :type ystart: int
    :param limit:
    :type limit: int

    :rtype: object
    """
    json_data = GetCurrentData.get_current_data(GetCurrentData, limit)
    print(json_data[len(json_data) - 5:])

    return json_data

def towdata_delete():  # noqa: E501
    """Deletes the current prediction data

     # noqa: E501


    :rtype: None
    """

    DeleteData.delete(DeleteData)

    return 'do some magic!'


def towdata_get(algorithm="LR"):  # noqa: E501
    """returns the prediction for the current dataset

    it will return the predicition for the fibonacci series from 1 to N, (the N should be configurable, but for next iterations. Window size should be configurable) # noqa: E501


    :rtype: InlineResponse200
    """
    prediction = GetPrediction.predict_data(GetPrediction, algorithm)
    return prediction


def towdata_post(body):  # noqa: E501
    """uploads data to train and predict over

    The body should be in .csv format so the server can read it # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """

    body = Body1.from_dict(connexion.request.get_json())  # noqa: E501
    SaveData.save(SaveData, body.csv)
    return "Done!"


def towdata_put(body):  # noqa: E501
    """Uploads live data to the server for predicition

    The data should be in a csv format # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """


    body = Body.from_dict(connexion.request.get_json())  # noqa: E501
    print(body)
    UpdateData.update(SaveData, body.csv)
