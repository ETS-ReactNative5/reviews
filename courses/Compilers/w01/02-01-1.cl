class Main {
    i: IO <- new IO;

    main(): Int {
        {
            i.out_string("Hello World!\n");
            1;
        }
    };
};
