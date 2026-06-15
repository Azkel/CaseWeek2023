# CaseWeek 2023 exercise: intentional bug for "failing pipeline" lab.
# Fix `true` → `True`, then wire this file into CI (see docs/exercises.md).
from django.test import TestCase


class AnimalTestCase(TestCase):
    def test_animals_can_speak(self):
        self.assertEqual(true, true)  # noqa: F821 — broken on purpose