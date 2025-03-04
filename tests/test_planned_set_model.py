import pytest

from styx import db
from styx.models import PlannedSet, SetType


@pytest.fixture
def sample_set_type(init_database):
    """Create sample set type to be able to reference it in planned set."""
    set1 = SetType(name="Warm-Up")
        
    db.session.add(set1)
    db.session.commit()
    
    return set1

@pytest.fixture
def sample_planned_set(init_database, sample_set_type):
    """Create sample planned set for testing."""
    set1 = sample_set_type
    planned_set = PlannedSet(set_type_id = set1.id,
                              min_rep_range=3,
                              max_rep_range=6)
        
    db.session.add(planned_set)
    db.session.commit()
    
    return planned_set


class TestPlannedSet:
    def test_planned_set_creation(self, init_database, sample_planned_set):
        """Verify planned set data initialization on creation.

        Given: A database with planned set and set type objects.
        When:  A planned set is retrieved from database with set type
        name "Warm-Up".
        Then:
            - Planned set is not null (exists in the database).
            - Set type name is "Warm-Up".
            - Min rep range is 3.
            - Max rep range is 6.
        """
        set1 = SetType.query.filter_by(name="Warm-Up").first()
        
        planned_set_from_db = \
            PlannedSet.query.filter_by(set_type_id=set1.id).first()

        assert planned_set_from_db is not None
        assert planned_set_from_db.set_type.name == "Warm-Up"
        assert planned_set_from_db.min_rep_range == 3
        assert planned_set_from_db.max_rep_range == 6

    def test_min_rep_range_validation(self, init_database, sample_set_type):
        """Verify than min range can't be a negative value.

        Given: A planned set object.
        When:  Min range is greater than max range.
        Then:  A Value Error is raised.
        """
        with pytest.raises(ValueError) as excinfo:
            PlannedSet(
                set_type=sample_set_type,
                min_rep_range=-1,
                max_rep_range=5
            )

        assert "negative" in str(excinfo.value)

    def test_max_rep_range_validation(self, init_database, sample_set_type):
        with pytest.raises(ValueError) as excinfo:
            PlannedSet(
                set_type=sample_set_type,
                min_rep_range=3,
                max_rep_range=-9
            )

        assert "negative" in str(excinfo.value)

    def test_max_less_than_min(self, init_database, sample_set_type):
        """Verify than min range can't be greater than max range.

        Given: A planned set object.
        When:  Min range is greater than max range.
        Then:  A Value Error is raised.
        """
        with pytest.raises(ValueError) as excinfo:
            PlannedSet(
                set_type=sample_set_type,
                max_rep_range=3,
                min_rep_range=5
            )
        assert "greater than maximum" in str(excinfo.value)

    def test_min_greater_than_max(self, init_database, sample_set_type):
        """Verify that max range can't be less than min range.

        Given: A planned set object.
        When:  Min range is greater than max range.
        Then:  A Value Error is raised.
        """
        # Note: there is a distinction between this test and 
        # the test before it. In the previous test we are 
        # checking the validator that was defined for the min_rep_range
        # field. While this test tests the validator for max_rep_range,
        # i.e. we are checking if max is initialized (improperly)
        # before min (test1), and checking if min is
        # initialized (improperly) before max (test 2).
        with pytest.raises(ValueError) as excinfo:
            PlannedSet(
                set_type=sample_set_type,
                min_rep_range=5,
                max_rep_range=3
            )
        assert "less than minimum" in str(excinfo.value)

    def test_equal_rep_range(self, init_database, sample_set_type):
        """Verify that min and max ranges can be equal.

        Given: A planned set object.
        When:  Min and Max range initialized with the same number.
        Then:  The planned set is inserted into the database successfully.
        """
        p_set = PlannedSet(
            set_type = sample_set_type,
            min_rep_range = 2,
            max_rep_range = 2
        )

        db.session.add(p_set)
        db.session.commit()

    def test_planned_set_repr(self, sample_planned_set, sample_set_type):
        """Verify the __repr__ method of the planned set model.

        Given: A planned set object.
        When:  The repr() function is called on the planned set object.
        Then:  A string representation matching the 
        expected format is returned, containing the set type name, and
        min and max ranges.
        """
        expected_repr = (
            f"PlannedSet(set_type={sample_set_type.name}, "
            f"min_rep_range=3, max_rep_range=6)"
        )
        
        assert repr(sample_planned_set) == expected_repr

    def test_planned_set_deletion(self,
                                  init_database,
                                  sample_set_type,
                                  sample_planned_set):
        """Verify planned set deletion functionality.

        Given: A planned set object.
        When:  Planned set is deleted from the database and changes 
        are committed.
        Then:  Planned set cannot be found in the database.
        """
        planned_set = sample_planned_set
        set1 = sample_set_type
        # Delete planned set
        db.session.delete(planned_set)
        db.session.commit()
        
        # Verify deletion
        assert PlannedSet.query.filter_by(set_type_id=set1.id).first() is None
