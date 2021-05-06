#define max_rounds 1000
#define max_favor 5
#define max_regen 30
#define max_poison 5
#define max_anger 5
#define max_heals 9999
#define pierce 1
#define shield_reduction 0.02
typedef long long int lint;

#ifdef BUILD_DLL
#define EXPORT __declspec(dllexport)
#else
#define EXPORT __declspec(dllimport)
#endif

lint min(lint x, lint y) { return (x<y?x:y); }

EXPORT int fight(lint pet1_dmg, lint pet1_hp, int pet1_regen, int pet1_heal,
            lint pet2_dmg, lint pet2_hp, int pet2_regen, int pet2_heal,
            float bonus_reflect, float bonus_converge,
            float runes_poison, float runes_anger, float runes_favor,
            lint op_hp, float op_shield, lint op_base_dmg, int op_dmg)
{
    float favor_stack = 1;
    float anger_stack = 1;
    lint pet1Damage = pet1_dmg;
    lint pet2Damage = pet2_dmg;
    lint pet1HP = pet1_hp;
    lint pet2HP = pet2_hp;
    lint opponentHp = op_hp;
    float shield = op_shield;

    int usedHeals = 0;

    for (int i = 1; i <= max_rounds; ++i)
    {
        // Before the fight
        if (shield > 0)
        {
            pet1Damage = pet1Damage*shield_reduction;
            pet2Damage = pet2Damage*shield_reduction;
        }

        int pet1Reflect = min(pet1Damage/2, (lint)(op_base_dmg * bonus_reflect));
        int pet2Reflect = min(pet2Damage/2, (lint)(op_base_dmg * bonus_reflect));
        float converge = (pet1Damage + pet2Damage) * bonus_converge;

        // Regen
        pet1HP += i <= max_regen ? pet1_regen : 0;
        pet2HP += i <= max_regen ? pet2_regen : 0;

        // Fight
        lint damage = pet1Damage + pet1Reflect + pet2Damage + pet2Reflect + converge;
        opponentHp -= damage;

        // Pets below 0 hp do not receive any damage. If one pet is dead the other one will take double damage.
        lint d1 = op_dmg * (pet2HP <= 0 ? 2 : 1) / favor_stack;
        lint d2 = op_dmg * (pet1HP <= 0 ? 2 : 1) / favor_stack;
        pet1HP -= d1;
        pet2HP -= d2;

        // Heal
        while (usedHeals < max_heals && (pet1HP <= 0 || pet2HP <= 0))
        {
            pet1HP += pet1_heal;
            pet2HP += pet2_heal;
            usedHeals += 1;
        }

        // Exit condition
        if (opponentHp <= 0) break;

        // After fight
        float poison_stack = 1 + (runes_poison * (i % (max_poison + 1)));
        anger_stack +=  i <= max_anger ? runes_anger : 0;
        favor_stack +=  i <= max_favor ? runes_favor : 0;
        shield = shield > pierce ? shield - pierce : 0;

        // Update pet dmg
        pet1Damage = (lint)(pet1_dmg * poison_stack * anger_stack);
        pet2Damage = (lint)(pet2_dmg * poison_stack * anger_stack);
    }
    return usedHeals;
}

// TODO
// Instead of shared lib, fight.c could be compiled
// as executable and python could feed this exe
// thru pipe but I'm not sure about this solution
//int main()
//{
//    int r = 0;
//    r = fight(3132840264, 73837, 26285, 28796,
//                3132840264, 73837, 26285, 28796,
//                9.92, 0.84,
//                0.0975, 0, 0.074,
//                351555789279, 0, 13528744, 344983);
//    printf("%d", r); //Just To check math
//
//    lint pet1_dmg; lint pet1_hp; int pet1_regen; int pet1_heal;
//    lint pet2_dmg; lint pet2_hp; int pet2_regen; int pet2_heal;
//    float bonus_reflect; float bonus_converge;
//    float runes_poison; float runes_anger; float runes_favor;
//    lint op_hp; float op_shield; lint op_base_dmg; int op_dmg;
//    while (1)
//    {
//        std::cin>>pet1_dmg;
//        std::cin>>pet1_hp;
//        std::cin>>pet1_regen;
//        std::cin>>pet1_heal;
//
//        std::cin>>pet2_dmg;
//        std::cin>>pet2_hp;
//        std::cin>>pet2_regen;
//        std::cin>>pet2_heal;
//
//        std::cin>>bonus_reflect;
//        std::cin>>bonus_converge;
//
//        std::cin>>runes_poison;
//        std::cin>>runes_anger;
//        std::cin>>runes_favor;
//
//        std::cin>>op_hp;
//        std::cin>>op_shield;
//        std::cin>>op_base_dmg;
//        std::cin>>op_dmg;
//
//        std::cout<<fight(pet1_dmg, pet1_hp, pet1_regen, pet1_heal,
//                            pet2_dmg, pet2_hp, pet2_regen, pet2_heal,
//                            bonus_reflect, bonus_converge,
//                            runes_poison, runes_anger, runes_favor,
//                            op_hp, op_shield, op_base_dmg, op_dmg);
//    }
//}