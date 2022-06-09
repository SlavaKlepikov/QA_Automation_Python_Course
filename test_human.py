import pytest
import logging
from code_for_testing import Human

logger = logging.getLogger()
logger.setLevel('INFO')


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize('age_param', [0, 1, 104, 105, 200])
def test_human_init_age(age_param):
    """
    Description: Check the 'age' method for the Human object
    Pre-conditions:
    1. Human object is created with valid argument 'age' = <value> and all mandatory arguments
    Steps:
    1. Call 'age' method for Human object
    Expected:
    1. Method 'age' returns <value>
    """
    logger.info('\nTEST START')
    human = Human(name="Maks", age=age_param, gender="female")
    assert human.age == age_param, f"\nAge is not as expected\nActual: {human.age}\nExpected:{age_param}"


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize('age_param', [0, 52, 104])
def test_human_grow_age(age_param):
    """
    Description: Check the 'grow' method for the Human object
    """
    logger.info('\nTEST START')
    human = Human(name="Maks", age=age_param, gender="female")
    human.grow()
    assert human.age == age_param + 1, f"\nAge is not as expected\nActual: {human.age}\nExpected:{age_param + 1}"


@pytest.mark.regression
def test_human_multiple_grow_age():
    """
     Description: Check the 'grow' method twice for the Human object
    """
    logger.info('\nTEST START')
    human = Human(name="Maks", age=25, gender="female")
    human.grow()
    human.grow()
    assert human.age == 27, f"\nAge is not as expected\nActual: {human.age}\nExpected:{27}"


@pytest.mark.smoke
@pytest.mark.parametrize('age_param', [105, 200])
def test_human_grow_dead(age_param):
    """
     Description: Check the 'status' method for the Human object in case 'dead'
    """
    logger.info('\nTEST START')
    human = Human(name="Maks", age=age_param, gender="female")
    human.grow()
    assert human.status == "dead", f"\nAge is not as expected\nActual: {human.status }\nExpected:dead"


@pytest.mark.smoke
def test_human_grow_dead():
    """
    Description: Check the 'raise Exception' for 'grow' method  in case Human object is already 'dead'
    """
    logger.info('\nTEST START')
    human = Human(name="Maks", age=105, gender="female")
    human.grow()
    with pytest.raises(Exception):
        human.grow()


@pytest.mark.smoke
@pytest.mark.regression
def test_human_init_status():
    """
    Description: Check the 'status' method for the Human object in case 'alive'
    """
    logger.info('\nTEST START')
    human = Human(name="Maks", age=25, gender="female")
    assert human.status == "alive", f"\nAge is not as expected\nActual: {human.status }\nExpected:alive"


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize('gender_param', ["male", "female"])
def test_human_init_gender(gender_param):
    """
    Description: Check the 'gender' method for the Human object
    """
    logger.info('\nTEST START')
    human = Human(name="Maks", age=25, gender=gender_param)
    assert human.gender == gender_param


@pytest.mark.regression
@pytest.mark.parametrize("init_gender_param, gender_param",
                         [("male", "female"), ("female", "male"), ("male", "male"), ("female", "female"),
                          ("other", "female"), ("other", "male")])
def test_human_gender_(init_gender_param, gender_param):
    """
    Description: Check the 'gender' method for different available values
    """
    logger.info('\nTEST START')
    human = Human(name="Maks", age=25, gender=init_gender_param)
    human.gender = gender_param
    assert human.gender == gender_param


@pytest.mark.regression
@pytest.mark.parametrize("init_gender_param, gender_param",
                         [("male", ""), ("male", "other"), ("female", ""), ("female", "other")])
def test_human_gender_change_raises_exception(init_gender_param, gender_param):
    """
    Description: Check that the 'gender' method is raised Exception in case invalid value
    """
    logger.info('\nTEST START')
    human = Human(name="Maks", age=25, gender=init_gender_param)
    with pytest.raises(Exception):
        human.gender = gender_param


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize('name_param', ["", " ", "M", "Max", "Maxsimuss", "Maxsimusssssssssssss"])
def test_human_init_name(name_param):
    """
    Description: Check the 'name' method for the Human object
    """
    logger.info('\nTEST START')
    human = Human(name=name_param, age=25, gender="female")
    assert human.name == name_param


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize('name_param', ["M", "Max", "Maks", "Maxsimuss"])
def test_human_change_name(name_param):
    """
    Description: Check the 'change_name' method for the Human object
    """
    logger.info('\nTEST START')
    human = Human(name="Maks", age=25, gender="male")
    human.change_name(name_param)
    assert human.name == name_param


@pytest.mark.regression
def test_human_change_name_exception_died():
    """
    Description: Check that the 'change_name' method is raised Exception in case Human object is already died
    """
    logger.info('\nTEST START')
    human = Human(name="Maks", age=105, gender="male")
    human.grow()
    with pytest.raises(Exception):
        human.change_name("Max")


@pytest.mark.regression
@pytest.mark.parametrize('name_param', [" ", "m", "max", "mAX"])
def test_change_name_isupper_raises_exception(name_param):
    """
    Description: Check that the 'change_name' method is raised Exception in case invalid 'name'
    """
    logger.info('\nTEST START')
    human = Human(name="Maks", age=25, gender="male")
    with pytest.raises(SyntaxError):
        human.change_name(name_param)


@pytest.mark.regression
def test_change_name_len_raises_exception():
    """
    Description: Check that the 'change_name' method is raised Exception in case name > 10
    """
    logger.info('\nTEST START')
    human = Human(name="Maks", age=25, gender="male")
    name = "M" + "m" * 9
    with pytest.raises(SyntaxError):
        human.change_name(name)


@pytest.mark.regression
def test_change_name_len_isupper_raises_exception():
    """
    Description: Check that the 'change_name' method is raised Exception in case invalid 'name' and 'name' > 10
    """
    logger.info('\nTEST START')
    human = Human(name="Maks", age=25, gender="male")
    name = "m" * 10
    with pytest.raises(SyntaxError):
        human.change_name(name)


@pytest.mark.regression
def test_human_init_friends(human_object):
    """
    Description: Check the 'friends' method is [] in case no friends
    """
    logger.info('\nTEST START')
    assert human_object.friends == []


@pytest.mark.smoke
@pytest.mark.regression
def test_human_no_friends(human_object):
    """
    Description: Check the 'friends' method is [] in case friends is not added
    """
    logger.info('\nTEST START')
    friends = Human(name="Gina", age=18, gender="female")
    assert human_object.friends == []


@pytest.mark.smoke
@pytest.mark.regression
def test_human_make_friends(human_object):
    """
    Description: Check the 'friends' method for the Human object
    """
    logger.info('\nTEST START')
    friend = Human(name="Gina", age=18, gender="female")
    human_object.make_friends(friend)
    assert human_object.friends == [friend]


@pytest.mark.regression
def test_human_multiple_make_friends(human_object):
    """
    Description: Check the 'friends' method for the Human object in case multiple friends
    """
    logger.info('\nTEST START')
    friends1 = Human(name="Gina", age=18, gender="female")
    friends2 = Human(name="Gina", age=18, gender="female")
    human_object.make_friends(friends1)
    human_object.make_friends(friends2)
    assert human_object.friends == [friends1, friends2]


@pytest.mark.regression
def test_human_the_same_make_friends(human_object):
    """
    Description: Check the 'friends' method for the Human object in case the same multiple friends
    """
    logger.info('\nTEST START')
    friends = Human(name="Gina", age=18, gender="female")
    human_object.make_friends(friends)
    human_object.make_friends(friends)
    assert human_object.friends == [friends, friends]


@pytest.mark.regression
def test_human_friends_after_died(human_object):
    """
    Description: Check the 'make_friends' method for the Human object in case friend is died
    """
    logger.info('\nTEST START')
    friend = Human(name="Gina", age=105, gender="female")
    human_object.make_friends(friend)
    friend.grow()
    assert human_object.friends == [friend]


@pytest.mark.regression
def test_cross_friends_make_friends(human_object):
    """
    Description: Check the 'friends' method in case Friends is crossed
    """
    logger.info('\nTEST START')
    friend = Human(name="Gina", age=18, gender="female")
    human_object.make_friends(friend)
    friend.make_friends(human_object)
    assert human_object.friends == [friend]
    assert friend.friends == [human_object]


@pytest.mark.regression
def test_friends_himself_make_friends(human_object):
    """
    Description: Check the "friends" method if the Person is a friend for himself.
    """
    logger.info('\nTEST START')
    human_object.make_friends(human_object)
    assert human_object.friends == [human_object]


@pytest.mark.under_clarification
@pytest.mark.negative
@pytest.mark.parametrize('age_param', ["", " ", "100", 12.4, True])
def test_human_invalid_age(age_param):
    """
    Description:  Check the 'age' method for the Human object in case invalid values
    """
    logger.info('\nTEST START')
    human = Human(name="Max", age=age_param, gender="female")
    assert human.age == age_param, f"\nAge is not as expected\nActual: {human.age}\nExpected:''"


@pytest.mark.under_clarification
@pytest.mark.negative
@pytest.mark.parametrize('name_param', ["", 123, " ", "_#@$@#%", "Ma x", True])
def test_human_invalid_name(name_param):
    """
    Description:  Check the 'name' method for the Human object in case invalid values
    """
    logger.info('\nTEST START')
    human = Human(name=name_param, age=25, gender="female")
    assert human.name == name_param, f"\nAge is not as expected\nActual: {human.name}\nExpected:''"


@pytest.mark.under_clarification
@pytest.mark.negative
@pytest.mark.parametrize('gender_param', ["", 123, " ", "_#@$@#%", "Ma x", False])
def test_human_invalid_gender(gender_param):
    """
    Description:  Check the 'gender' method for the Human object in case invalid values
    """
    logger.info('\nTEST START')
    human = Human(name="Max", age=25, gender=gender_param)
    assert human.gender == gender_param, f"\nAge is not as expected\nActual: {gender_param}\nExpected:''"