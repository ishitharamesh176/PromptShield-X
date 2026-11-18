from attack_patterns import detect_regex_attacks
from attack_generator import get_random_variations


def run_generated_attack_test(number_of_attacks=20):

    attacks = get_random_variations(number_of_attacks)

    detected = 0
    missed = 0

    print("\n========================================")
    print("       PROMPTSHIELD X")
    print("   GENERATED ATTACK TEST LAB")
    print("========================================")

    for i, prompt in enumerate(attacks, 1):

        matches = detect_regex_attacks(prompt)

        if matches:

            decision = "BLOCK"
            status = "DETECTED"
            detected += 1

        else:

            decision = "ALLOW"
            status = "MISSED"
            missed += 1

        print("\n----------------------------------------")
        print("Attack #", i)
        print("Prompt:", prompt)
        print("Decision:", decision)
        print("Status:", status)

    detection_rate = (detected / len(attacks)) * 100
    miss_rate = (missed / len(attacks)) * 100

    print("\n========================================")
    print("       GENERATED ATTACK RESULTS")
    print("========================================")

    print("Attacks generated :", len(attacks))
    print("Attacks detected  :", detected)
    print("Attacks missed    :", missed)
    print("Detection rate    :", f"{detection_rate:.2f}%")
    print("Miss rate         :", f"{miss_rate:.2f}%")

    print("========================================")


if __name__ == "__main__":

    run_generated_attack_test(20)