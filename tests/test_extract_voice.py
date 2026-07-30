#!/usr/bin/env python3
# Copyright 2026 Google LLC
#
# Unit tests for extract_voice.py helper engine

import os
import sys
import unittest

# Add scripts folder to sys.path
SCRIPT_DIR = os.path.join(os.path.dirname(__file__), "..", "skills", "extract-human-voice", "scripts")
sys.path.insert(0, os.path.abspath(SCRIPT_DIR))

from extract_voice import sanitize_text, analyze_linguistics, get_tool_paths

class TestExtractVoice(unittest.TestCase):

    def test_sanitize_text_emails_and_domains(self):
        raw = "Contact user@example.com or visit https://subdomain.google.com/test for info."
        clean = sanitize_text(raw)
        self.assertIn("<EMAIL>", clean)
        self.assertNotIn("user@example.com", clean)
        self.assertIn("<INTERNAL_URL>", clean)

    def test_sanitize_text_expanded_secrets(self):
        raw_github_pat = "Token: github_pat_11AAAAAAA0000000000000_1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        raw_anthropic = "Key: sk-ant-api03-1234567890abcdefghijklmnopqrstuvwxyz12345678"
        raw_openai = "Key: sk-1234567890abcdefghijklmnopqrstuvwxyz12"
        raw_aws = "Key: AKIA1234567890ABCDEF"
        raw_gitlab = "Key: glpat-1234567890abcdefghij"

        self.assertIn("<REDACTED_GITHUB_PAT>", sanitize_text(raw_github_pat))
        self.assertIn("<REDACTED_ANTHROPIC_KEY>", sanitize_text(raw_anthropic))
        self.assertIn("<REDACTED_OPENAI_KEY>", sanitize_text(raw_openai))
        self.assertIn("<REDACTED_AWS_ACCESS_KEY>", sanitize_text(raw_aws))
        self.assertIn("<REDACTED_GITLAB_PAT>", sanitize_text(raw_gitlab))

    def test_get_tool_paths_structure(self):
        paths = get_tool_paths()
        expected_keys = ["antigravity-cli", "gemini-cli", "claude-code", "cline", "roo-code", "aider", "cursor"]
        for key in expected_keys:
            self.assertIn(key, paths)
            self.assertTrue(isinstance(paths[key], str))

    def test_sanitize_text_ipv6(self):
        raw_ipv6 = "Server located at 2001:0db8:85a3:0000:0000:8a2e:0370:7334 or ::1"
        clean = sanitize_text(raw_ipv6)
        self.assertIn("<IP_ADDRESS>", clean)
        self.assertNotIn("2001:0db8:85a3:0000:0000:8a2e:0370:7334", clean)

    def test_sanitize_text_extra_names(self):
        raw_text = "Please reach out to Alice and Bob regarding deployment."
        extra_names = [("Alice", "<USER_NAME>"), ("Bob", "<USER_NICKNAME>")]
        clean = sanitize_text(raw_text, extra_names=extra_names)
        self.assertIn("<USER_NAME>", clean)
        self.assertIn("<USER_NICKNAME>", clean)
        self.assertNotIn("Alice", clean)
        self.assertNotIn("Bob", clean)

    def test_analyze_linguistics(self):
        sample_prompts = [
            "Please customise and optimise the organisation behaviour.",
            "Please customise and optimise the colour palette.",
            "This table is useless and broken... why is it so slow??",
            "Review this repo and write tests."
        ]
        stats = analyze_linguistics(sample_prompts)
        self.assertEqual(stats["spelling"], "British/Commonwealth")
        self.assertGreater(stats["critique_count"], 0)
        self.assertGreater(stats["average_word_count"], 0)

if __name__ == "__main__":
    unittest.main()
